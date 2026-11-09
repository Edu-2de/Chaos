import pytest
from django.db import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Type
from products.views import TypeViewSet


@pytest.mark.django_db
def test_list_types_return_success():
    Type.objects.create(name="Type")
    Type.objects.create(name="Type2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = TypeViewSet.as_view({"get": "list"})

    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Type"


@pytest.mark.django_db
def test_create_duplicate_return_fail():
    Type.objects.create(name="Type")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Type"})

    view = TypeViewSet.as_view({"post": "create"})

    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_lower_return_fail():
    Type.objects.create(name="Type")

    with pytest.raises(IntegrityError):
        Type.objects.create(name="type")
