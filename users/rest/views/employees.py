from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from redisio.users.services import EmployeeRedisServices
from users.models import Employee
from users.rest.serializers.employees import PrivateEmployeeListSerializer


class PrivateEmployeeList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PrivateEmployeeListSerializer

    def get_queryset(self):
        return None

    def get(self, request, *args, **kwargs):
        search = self.request.query_params.get("search", "")
        employee_redis_search = EmployeeRedisServices()

        if not search:
            return Response(data=employee_redis_search.all())

        return Response(data=employee_redis_search.search(name=search))


class PrivateEmployeeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PrivateEmployeeListSerializer
    queryset = Employee.objects.filter()
    lookup_field = "uid"
