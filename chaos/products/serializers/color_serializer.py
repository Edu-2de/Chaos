from rest_framework import serializers

from products.models import Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:  # type:ignore
        model = Color
        fields = "__all__"
