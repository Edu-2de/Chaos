import pytest
from rest_framework.test import APIRequestFactory

from products.models import Product
from products.views import ProductViewSet, ProductViewSetWithParams

from .factories import BrandFactory, CategoryFactory, ProductFactory, TypeFactory


@pytest.mark.django_db
def test_list_products_return_success():
    product = ProductFactory()
    ProductFactory()

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ProductViewSet.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 2
    assert response.data["results"][0]["name"] == product.name


@pytest.mark.django_db
def test_create_product_return_success():
    factory = APIRequestFactory()
    request = factory.post(
        "/fake-url/",
        {
            "name": "Product",
            "description": "Description",
            "category": CategoryFactory().id,
            "type": TypeFactory().id,
            "brand": BrandFactory().id,
        },
    )

    view = ProductViewSet.as_view()
    response = view(request)

    assert response.status_code == 201
    assert response.data["name"] == "Product"


@pytest.mark.django_db
def test_create_product_without_name_return_fail():
    factory = APIRequestFactory()
    request = factory.post(
        "/fake-url/",
        {
            "description": "Description",
            "category": CategoryFactory().id,
            "type": TypeFactory().id,
            "brand": BrandFactory().id,
        },
    )

    view = ProductViewSet.as_view()
    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_retrieve_product_return_success():
    product = ProductFactory()

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ProductViewSetWithParams.as_view()
    response = view(request, pk=product.id)

    assert response.status_code == 200
    assert response.data["name"] == product.name


@pytest.mark.django_db
def test_retrieve_product_not_found():
    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ProductViewSetWithParams.as_view()
    response = view(request, pk=999)

    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_product_return_success():
    product = ProductFactory()

    factory = APIRequestFactory()
    request = factory.delete("/fake-url/")

    view = ProductViewSetWithParams.as_view()
    response = view(request, pk=product.id)

    assert response.status_code == 204
    assert not Product.objects.filter(pk=product.id).exists()


@pytest.mark.django_db
def test_update_product_return_success():
    product = ProductFactory()

    factory = APIRequestFactory()
    request = factory.put(
        "/fake-url/",
        {
            "name": "Product-new",
            "description": product.description,
            "category": product.category.id,
            "type": product.type.id,
            "brand": product.brand.id,
        },
    )

    view = ProductViewSetWithParams.as_view()
    response = view(request, pk=product.id)

    assert response.status_code == 200
    assert response.data["name"] == "Product-new"


@pytest.mark.django_db
def test_update_partial_product_return_success():
    product = ProductFactory()

    factory = APIRequestFactory()
    request = factory.patch("/fake-url/", {"name": "Product-1"})

    view = ProductViewSetWithParams.as_view()
    response = view(request, pk=product.id)

    assert response.status_code == 200
    assert response.data["name"] == "Product-1"
