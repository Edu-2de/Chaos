import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Brand
from products.views import BrandViewSet


@pytest.mark.django_db
def test_list_return_success():
    Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = BrandViewSet.as_view({"get": "list"})

    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Brand1"


@pytest.mark.django_db
def test_create_duplicate_name_fail():
    Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Brand1"})

    view = BrandViewSet.as_view({"post": "create"})

    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_brand_lower_return_fail():
    Brand.objects.create(name="Brand1")

    with pytest.raises(IntegrityError):
        Brand.objects.create(name="brand1")
