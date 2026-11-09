from rest_framework import viewsets

from products.models import Type
from products.serializers import TypeSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
