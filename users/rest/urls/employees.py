from django.urls import path

from ..views import employees

urlpatterns = [
    path(
        "/<uuid:uid>",
        employees.PrivateEmployeeDetail.as_view(),
        name="private-employee-detail",
    ),
    path("", employees.PrivateEmployeeList.as_view(), name="private-employee-list"),
]
