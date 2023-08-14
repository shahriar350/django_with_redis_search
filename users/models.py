import uuid

from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModelWithUID
from users.choices import EmployeeDepartment

User = get_user_model()


# Create your models here.
class Employee(BaseModelWithUID):
    uid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=300)
    department = models.CharField(choices=EmployeeDepartment.choices, max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
