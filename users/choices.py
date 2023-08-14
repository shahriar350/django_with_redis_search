from django.db import models


class EmployeeDepartment(models.TextChoices):
    DEVELOPMENT = (
        "DEVELOPMENT",
        "Development",
    )
    HumanResource = "Human Resource", "Humen Resource"
    IT = (
        "IT",
        "it",
    )
    ADMIN = "ADMIN", "Admin"
