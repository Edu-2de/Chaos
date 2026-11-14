from core.pagination import Pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Category
from products.serializers import CategorySerializer


class CategoryViewSet(APIView):
    def get(self, request):
        paginator = Pagination()
        queryset = Category.objects.all().order_by("name")
        page = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = CategorySerializer(page, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)


class CategoryViewSetWithParams(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=204)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if not serializer.is_valid():
            Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)
