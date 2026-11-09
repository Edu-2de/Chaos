from rest_framework import viewsets

from products.models import Color
from products.serializers import ColorSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
