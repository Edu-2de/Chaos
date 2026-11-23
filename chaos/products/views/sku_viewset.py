from core.pagination import Pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Sku
from products.serializers import SkuSerializer


class SkuViewSet(APIView):
    def get(self, request):
        paginator = Pagination()
        queryset = Sku.objects.all().order_by("id")
        page = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = SkuSerializer(page, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = SkuSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)


class SkuViewSetWithParams(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Sku, pk=pk)
        serializer = SkuSerializer(instance)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        instance = get_object_or_404(Sku, pk=pk)
        instance.delete()
        return Response(status=204)

    def put(self, request, pk):
        instance = get_object_or_404(Sku, pk=pk)
        serializer = SkuSerializer(instance, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = get_object_or_404(Sku, pk=pk)
        serializer = SkuSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)
