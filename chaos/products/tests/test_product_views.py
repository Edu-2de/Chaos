import pytest
from rest_framework.test import APIRequestFactory

from products.views import ProductViewSet

from .factories import ProductFactory


@pytest.mark.django_db
def test_list_products_return_success():
    product = ProductFactory()
    ProductFactory()

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ProductViewSet.as_view({"get": "list"})

    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["name"] == product.name
