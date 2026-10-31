from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:  # type:ignore
        model = Product
        fields = "__all__"
