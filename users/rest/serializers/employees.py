from django.contrib.auth import get_user_model
from rest_framework import serializers

from redisio.users.services import EmployeeRedisServices
from users.models import Employee, Category
from users.rest.serializers.categories import PrivateCategorySerializer

User = get_user_model()


class PrivateEmployeeListSerializer(serializers.ModelSerializer):
    category = PrivateCategorySerializer(read_only=True)
    category_uid = serializers.SlugRelatedField(
        write_only=True, queryset=Category.objects.filter(), slug_field="uid"
    )

    class Meta:
        model = Employee
        fields = (
            "uid",
            "name",
            "department",
            "category",
            "category_uid",
        )
        read_only_fields = ("category",)

    def create(self, validated_data):
        validated_data["category"] = validated_data.pop("category_uid")
        employee: Employee = super().create(validated_data)

        # a saving instance to redis
        employee_redis_search = EmployeeRedisServices()
        employee_redis_search.create(instance=employee)
        return employee
