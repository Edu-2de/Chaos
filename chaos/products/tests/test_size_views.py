import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Size
from products.views import SizeViewSet, SizeViewSetWithParams


@pytest.mark.django_db
def test_list_sizes_return_success():
    Size.objects.create(name="Size1")
    Size.objects.create(name="Size2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SizeViewSet.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 2
    assert response.data["results"][0]["name"] == "Size1"


@pytest.mark.django_db
def test_create_size_return_success():
    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Size1"})

    view = SizeViewSet.as_view()
    response = view(request)

    assert response.status_code == 201
    assert response.data["name"] == "Size1"


@pytest.mark.django_db
def test_create_duplicate_size_return_fail():
    Size.objects.create(name="Size1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Size1"})

    view = SizeViewSet.as_view()
    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_size_lower_return_fail():
    Size.objects.create(name="Size1")

    with pytest.raises(IntegrityError):
        Size.objects.create(name="size1")


@pytest.mark.django_db
def test_retrieve_size_return_success():
    instance = Size.objects.create(name="Size1")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SizeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Size1"


@pytest.mark.django_db
def test_retrieve_size_not_found():
    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = SizeViewSetWithParams.as_view()
    response = view(request, pk=999)

    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_size_return_success():
    instance = Size.objects.create(name="Size1")

    factory = APIRequestFactory()
    request = factory.delete("/fake-url/")

    view = SizeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 204
    assert not Size.objects.filter(pk=instance.id).exists()


@pytest.mark.django_db
def test_update_size_return_success():
    instance = Size.objects.create(name="Size1")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "Size-new"})

    view = SizeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Size-new"


@pytest.mark.django_db
def test_update_duplicate_size_return_fail():
    instance = Size.objects.create(name="Size1")
    Size.objects.create(name="SizeAlreadyExists")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "SizeAlreadyExists"})

    view = SizeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_partial_size_return_success():
    instance = Size.objects.create(name="Size1")

    factory = APIRequestFactory()
    request = factory.patch("/fake-url/", {"name": "Size-1"})

    view = SizeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Size-1"
