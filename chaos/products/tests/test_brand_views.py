import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Brand
from products.views import BrandViewSet, BrandViewSetWithParams


@pytest.mark.django_db
def test_list_return_success():
    Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = BrandViewSet.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Brand1"


@pytest.mark.django_db
def test_create_duplicate_name_fail():
    Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Brand1"})

    view = BrandViewSet.as_view()
    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_brand_lower_return_fail():
    Brand.objects.create(name="Brand1")

    with pytest.raises(IntegrityError):
        Brand.objects.create(name="brand1")


@pytest.mark.django_db
def test_delete_brand_return_success():
    brand = Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.delete("/fake-url/")

    view = BrandViewSetWithParams.as_view()
    response = view(request, pk=brand.id)

    assert response.status_code == 204
    assert brand not in Brand.objects.all()


@pytest.mark.django_db
def test_update_brand_return_success():
    brand = Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "Brand-new"})

    view = BrandViewSetWithParams.as_view()
    response = view(request, pk=brand.id)

    assert response.status_code == 200
    assert response.data["name"] == "Brand-new"


@pytest.mark.django_db
def test_update_duplicate_brand_return_fail():
    brand = Brand.objects.create(name="Brand1")
    Brand.objects.create(name="BrandAlreadyExists")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "BrandAlreadyExists"})

    view = BrandViewSetWithParams.as_view()
    response = view(request, pk=brand.id)

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_partial_brand_return_success():
    brand = Brand.objects.create(name="Brand1")

    factory = APIRequestFactory()
    request = factory.patch("/fake-url", {"name": "Brand-1"})

    view = BrandViewSetWithParams.as_view()
    response = view(request, pk=brand.id)

    assert response.status_code == 200
    assert response.data["name"] == "Brand-1"
