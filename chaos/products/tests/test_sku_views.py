import pytest
from rest_framework.test import APIRequestFactory

from products.views import SkuViewSet

from .factories import SkuFactory


@pytest.mark.django_db
def test_list_skus_return_success():
    sku = SkuFactory()

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SkuViewSet.as_view({"get": "list"})

    response = view(request)
    assert response.status_code == 200
    assert response.data[0]["barcode"] == sku.barcode
