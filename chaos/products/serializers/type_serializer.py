from rest_framework import serializers

from products.models import Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:  # type:ignore
        model = Type
        fields = "__all__"
