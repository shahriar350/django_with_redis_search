from django.urls import path

from ..views import categories


urlpatterns = [
    path(
        "/<uuid:uid>",
        categories.PrivateCategoryDetail.as_view(),
        name="private-category-detail",
    ),
    path("", categories.PrivateCategoryList.as_view(), name="private-category-list"),
]
