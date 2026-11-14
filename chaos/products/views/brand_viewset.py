from core.pagination import Pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Brand
from products.serializers import BrandSerializer


class BrandViewSet(APIView):
    def get(self, request):
        paginator = Pagination()
        queryset = Brand.objects.all().order_by("name")
        page = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = BrandSerializer(page, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)


class BrandViewSetWithParams(APIView):
    def get(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def delete(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return Response(status=204)

    def put(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)
