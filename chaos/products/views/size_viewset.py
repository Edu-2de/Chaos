from core.pagination import Pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Size
from products.serializers import SizeSerializer


class SizeViewSet(APIView):
    def get(self, request):
        paginator = Pagination()
        queryset = Size.objects.all().order_by("name")
        page = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = SizeSerializer(page, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = SizeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)


class SizeViewSetWithParams(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Size, pk=pk)
        serializer = SizeSerializer(instance)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        instance = get_object_or_404(Size, pk=pk)
        instance.delete()
        return Response(status=204)

    def put(self, request, pk):
        instance = get_object_or_404(Size, pk=pk)
        serializer = SizeSerializer(instance, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = get_object_or_404(Size, pk=pk)
        serializer = SizeSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)
