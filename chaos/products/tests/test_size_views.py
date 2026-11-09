import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Size
from products.views import SizeViewSet


@pytest.mark.django_db
def list_colors_return_success():
    Size.objects.create(name="Size1")
    Size.objects.create(name="Size2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SizeViewSet.as_view({"get": "list"})

    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Size1"


@pytest.mark.django_db
def create_duplicate_return_fail():
    Size.objects.create(name="Size1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url", {"name": "Size1"})

    view = SizeViewSet.as_view({"post": "create"})

    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_color_lower_return_fail():
    Size.objects.create(name="Size1")

    with pytest.raises(IntegrityError):
        Size.objects.create(name="Size1")
