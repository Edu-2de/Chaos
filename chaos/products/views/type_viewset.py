from core.pagination import Pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Type
from products.serializers import TypeSerializer


class TypeViewSet(APIView):
    def get(self, request):
        paginator = Pagination()
        queryset = Type.objects.all().order_by("name")
        page = paginator.paginate_queryset(queryset=queryset, request=request)

        serializer = TypeSerializer(page, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = TypeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)


class TypeViewSetWithParams(APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(instance)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        instance = get_object_or_404(Type, pk=pk)
        instance.delete()
        return Response(status=204)

    def put(self, request, pk):
        instance = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(instance, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=200)
