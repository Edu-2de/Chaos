from django.urls import include, path
from rest_framework.routers import DefaultRouter

from chaos.products.views.size_viewset import SizeViewSet
from chaos.products.views.type_viewset import TypeViewSet

from .views import BrandViewSet, CategoryViewSet, ColorViewSet

router = DefaultRouter()
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"colors", ColorViewSet, basename="color")
router.register(r"sizes", SizeViewSet, basename="size")
router.register(r"type", TypeViewSet, basename="type")

urlpatterns = [path("", include(router.urls))]
