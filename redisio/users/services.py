from collections import deque
from typing import List

from redisio.users.schemas import EmployeePydantic
from users.models import Employee


class EmployeeRedisServices:
    def create(self, instance: Employee = None, serialize_data: dict = None):
        serialized_data = serialize_data
        # check if instance, make this instance to serialized data (json)
        if instance:
            from users.rest.serializers.employees import PrivateEmployeeListSerializer

            serialized_data = PrivateEmployeeListSerializer(instance).data

        # if saved to json, saved to redis using pydantic data. Same as Python Pydantic.
        new_employee_to_redis_save = EmployeePydantic(
            uid=serialized_data.get("uid"),
            name=serialized_data.get("name"),
            department=serialized_data.get("uid"),
            category=serialized_data.get("category"),
        )
        new_employee_to_redis_save.save()

    def search(self, name) -> List[dict]:
        # search employee name
        # use * for find name startswith, * means all character will be accepted after searching name
        # redis by default case in-sensitive.
        employee_from_redis = EmployeePydantic.find(EmployeePydantic.name % f"{name}*")

        # push that searching data into python queue
        response_data = deque(maxlen=employee_from_redis.count())
        for employee in employee_from_redis.all():
            response_data.appendleft(employee.dict(exclude={"pk"}))
        return list(response_data)

    def all(self) -> List[dict]:
        # get all employee value
        employee_from_redis = EmployeePydantic.find()
        response_data = deque(maxlen=employee_from_redis.count())
        for employee in employee_from_redis.all():
            response_data.appendleft(employee.dict(exclude={"pk"}))
        return list(response_data)
