from rest_framework import serializers

from products.models import Size


class SizeSerializer(serializers.ModelSerializer):
    class Meta:  # type:ignore
        model = Size
        fields = "__all__"
