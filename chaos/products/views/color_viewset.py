from core.pagination import Pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Color
from products.serializers import ColorSerializer


class ColorViewSet(APIView):
    def get(self, request):
        paginator = Pagination()
        queryset = Color.objects.all().order_by("name")
        page = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = ColorSerializer(page, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)


class ColorViewSetWithParams(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Color, pk=pk)
        serializer = ColorSerializer(instance)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        instance = get_object_or_404(Color, pk=pk)
        instance.delete()
        return Response(status=204)

    def put(self, request, pk):
        instance = get_object_or_404(Color, pk=pk)
        serializer = ColorSerializer(instance, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = get_object_or_404(Color, pk=pk)
        serializer = ColorSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)
