from rest_framework import serializers

from products.models import Sku


class SkuSerializer(serializers.ModelSerializer):
    class Meta:  # type:ignore
        model = Sku
        fields = "__all__"
