from rest_framework import serializers

from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:  # type: ignore
        model = Category
        fields = "__all__"
