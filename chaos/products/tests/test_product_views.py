import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Product
from products.views import ProductViewSet


@pytest.mark.django_db
def list_colors_return_success():
    Product.objects.create(name="Product1")
    Product.objects.create(name="Product2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ProductViewSet.as_view({"get": "list"})

    response = view(request)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Product1"
