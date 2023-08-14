import uuid

from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModelWithUID
from users.choices import EmployeeDepartment

User = get_user_model()


class Category(BaseModelWithUID):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Name: {self.name}"


# Create your models here.
class Employee(BaseModelWithUID):
    name = models.CharField(max_length=300)
    department = models.CharField(choices=EmployeeDepartment.choices, max_length=25)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Name: {self.name}"
