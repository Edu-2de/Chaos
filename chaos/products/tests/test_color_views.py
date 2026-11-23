import pytest
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory

from products.models import Color
from products.views import ColorViewSet, ColorViewSetWithParams


@pytest.mark.django_db
def test_list_colors_return_success():
    Color.objects.create(name="Color1")
    Color.objects.create(name="Color2")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ColorViewSet.as_view()
    response = view(request)

    assert response.status_code == 200
    assert len(response.data["results"]) == 2
    assert response.data["results"][0]["name"] == "Color1"


@pytest.mark.django_db
def test_create_color_return_success():
    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Color1"})

    view = ColorViewSet.as_view()
    response = view(request)

    assert response.status_code == 201
    assert response.data["name"] == "Color1"


@pytest.mark.django_db
def test_create_duplicate_color_return_fail():
    Color.objects.create(name="Color1")

    factory = APIRequestFactory()
    request = factory.post("/fake-url/", {"name": "Color1"})

    view = ColorViewSet.as_view()
    response = view(request)

    assert response.status_code == 400
    assert "name" in response.data


@pytest.mark.django_db
def test_create_duplicate_color_lower_return_fail():
    Color.objects.create(name="Color1")

    with pytest.raises(IntegrityError):
        Color.objects.create(name="color1")


@pytest.mark.django_db
def test_retrieve_color_return_success():
    instance = Color.objects.create(name="Color1")

    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ColorViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Color1"


@pytest.mark.django_db
def test_retrieve_color_not_found():
    factory = APIRequestFactory()
    request = factory.get("/fake-url/")

    view = ColorViewSetWithParams.as_view()
    response = view(request, pk=999)

    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_color_return_success():
    instance = Color.objects.create(name="Color1")

    factory = APIRequestFactory()
    request = factory.delete("/fake-url/")

    view = ColorViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 204
    assert not Color.objects.filter(pk=instance.id).exists()


@pytest.mark.django_db
def test_update_color_return_success():
    instance = Color.objects.create(name="Color1")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "Color-new"})

    view = ColorViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Color-new"


@pytest.mark.django_db
def test_update_duplicate_color_return_fail():
    instance = Color.objects.create(name="Color1")
    Color.objects.create(name="ColorAlreadyExists")

    factory = APIRequestFactory()
    request = factory.put("/fake-url/", {"name": "ColorAlreadyExists"})

    view = ColorViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_partial_color_return_success():
    instance = Color.objects.create(name="Color1")

    factory = APIRequestFactory()
    request = factory.patch("/fake-url/", {"name": "Color-1"})

    view = ColorViewSetWithParams.as_view()
    response = view(request, pk=instance.id)

    assert response.status_code == 200
    assert response.data["name"] == "Color-1"
