import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Type
from products.views import TypeViewSet, TypeViewSetWithParams


@pytest.mark.django_db
def test_list_types_return_success():
    Type.objects.create(name="Type1")
    Type.objects.create(name="Type2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = TypeViewSet.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 2
    assert response.data["results"][0]["name"] == "Type1"


@pytest.mark.django_db
def test_create_type_return_success():
    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Type1"})

    view = TypeViewSet.as_view()
    response = view(request)

    assert response.status_code == 201
    assert response.data["name"] == "Type1"


@pytest.mark.django_db
def test_create_duplicate_type_return_fail():
    Type.objects.create(name="Type1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Type1"})

    view = TypeViewSet.as_view()
    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_type_lower_return_fail():
    Type.objects.create(name="Type1")

    with pytest.raises(IntegrityError):
        Type.objects.create(name="type1")


@pytest.mark.django_db
def test_retrieve_type_return_success():
    instance = Type.objects.create(name="Type1")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = TypeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Type1"


@pytest.mark.django_db
def test_retrieve_type_not_found():
    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = TypeViewSetWithParams.as_view()
    response = view(request, pk=999)

    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_type_return_success():
    instance = Type.objects.create(name="Type1")

    factory = APIRequestFactory()
    request = factory.delete("/fake-url/")

    view = TypeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 204
    assert not Type.objects.filter(pk=instance.id).exists()


@pytest.mark.django_db
def test_update_type_return_success():
    instance = Type.objects.create(name="Type1")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "Type-new"})

    view = TypeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Type-new"


@pytest.mark.django_db
def test_update_duplicate_type_return_fail():
    instance = Type.objects.create(name="Type1")
    Type.objects.create(name="TypeAlreadyExists")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "TypeAlreadyExists"})

    view = TypeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_partial_type_return_success():
    instance = Type.objects.create(name="Type1")

    factory = APIRequestFactory()
    request = factory.patch("/fake-url/", {"name": "Type-1"})

    view = TypeViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Type-1"
