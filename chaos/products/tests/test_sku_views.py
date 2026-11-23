import pytest
from rest_framework.test import APIRequestFactory

from products.models import Sku
from products.views import SkuViewSet, SkuViewSetWithParams

from .factories import ColorFactory, ProductFactory, SizeFactory, SkuFactory


@pytest.mark.django_db
def test_list_skus_return_success():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SkuViewSet.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["barcode"] == sku.barcode


@pytest.mark.django_db
def test_create_sku_return_success():
    product = ProductFactory()
    color = ColorFactory()
    size = SizeFactory()

    factory = APIRequestFactory()
    request = factory.post(
        "/fake-url/",
        {
            "product": product.id,
            "color": color.id,
            "size": size.id,
            "price": "10.50",
            "stock": 3,
            "barcode": "123456789012",
        },
    )

    view = SkuViewSet.as_view()
    response = view(request)

    assert response.status_code == 201
    assert response.data["barcode"] == "123456789012"


@pytest.mark.django_db
def test_create_duplicate_barcode_return_fail():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.post(
        "/fake-url/",
        {
            "product": sku.product.id,
            "color": ColorFactory().id,
            "size": SizeFactory().id,
            "price": "10.50",
            "stock": 3,
            "barcode": sku.barcode,
        },
    )

    view = SkuViewSet.as_view()
    response = view(request)

    assert response.status_code == 400
    assert "barcode" in response.data


@pytest.mark.django_db
def test_retrieve_sku_return_success():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SkuViewSetWithParams.as_view()
    response = view(request, pk=sku.id)

    assert response.status_code == 200
    assert response.data["barcode"] == sku.barcode


@pytest.mark.django_db
def test_retrieve_sku_not_found():
    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SkuViewSetWithParams.as_view()
    response = view(request, pk=999)

    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_sku_return_success():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.delete("/fake-url/")

    view = SkuViewSetWithParams.as_view()
    response = view(request, pk=sku.id)

    assert response.status_code == 204
    assert not Sku.objects.filter(pk=sku.id).exists()


@pytest.mark.django_db
def test_update_partial_sku_return_success():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.patch("/fake-url/", {"stock": 99})

    view = SkuViewSetWithParams.as_view()
    response = view(request, pk=sku.id)

    assert response.status_code == 200
    assert response.data["stock"] == 99


@pytest.mark.django_db
def test_update_sku_invalid_price_return_fail():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.patch("/fake-url/", {"price": "not-a-number"})

    view = SkuViewSetWithParams.as_view()
    response = view(request, pk=sku.id)

    assert response.status_code == 400
    assert "price" in response.data
