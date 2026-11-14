from rest_framework import viewsets

from products.models import Sku
from products.serializers import SkuSerializer


class SkuViewSet(viewsets.ModelViewSet):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer
