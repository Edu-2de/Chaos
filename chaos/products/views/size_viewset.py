from rest_framework import viewsets

from products.models import Size
from products.serializers import SizeSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
