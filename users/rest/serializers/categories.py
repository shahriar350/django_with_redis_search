from rest_framework import serializers

from users.models import Category


class PrivateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("uid", "name")
