import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Color
from products.views import ColorViewSet


@pytest.mark.django_db
def list_colors_return_success():
    Color.objects.create(name="Color1")
    Color.objects.create(name="Color2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ColorViewSet.as_view({"get": "list"})

    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Color1"


@pytest.mark.django_db
def create_duplicate_return_fail():
    Color.objects.create(name="Color1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url", {"name": "Color1"})

    view = ColorViewSet.as_view({"post": "create"})

    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_color_lower_return_fail():
    Color.objects.create(name="Color1")

    with pytest.raises(IntegrityError):
        Color.objects.create(name="Color1")
