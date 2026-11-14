import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Category
from products.views import CategoryViewSet, CategoryViewSetWithParams


@pytest.mark.django_db
def test_list_categories_return_success():
    Category.objects.create(name="category1")
    Category.objects.create(name="category2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = CategoryViewSet.as_view()

    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 2
    assert response.data["results"][0]["name"] == "category1"


@pytest.mark.django_db
def test_create_duplicate_category_return_fail():
    Category.objects.create(name="category1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "category1"})

    view = CategoryViewSet.as_view()

    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_category_lower_return_fail():
    Category.objects.create(name="category1")

    with pytest.raises(IntegrityError):
        Category.objects.create(name="Category1")


@pytest.mark.django_db
def test_update_category_return_success():
    category = Category.objects.create(name="Category1")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "Category2"})

    view = CategoryViewSetWithParams.as_view()
    response = view(request, pk=category.id)

    assert response.data["name"] == "Category2"
