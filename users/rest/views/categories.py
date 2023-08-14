from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import Category
from users.rest.serializers.categories import PrivateCategorySerializer


class PrivateCategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateCategorySerializer
    queryset = Category.objects.filter()
    lookup_field = "uid"


class PrivateCategoryList(ListCreateAPIView):
    serializer_class = PrivateCategorySerializer
    queryset = Category.objects.filter()
