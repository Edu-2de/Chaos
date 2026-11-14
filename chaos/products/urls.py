from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BrandViewSet,
    CategoryViewSet,
    ColorViewSet,
    ProductViewSet,
    SizeViewSet,
    SkuViewSet,
    TypeViewSet,
)

router = DefaultRouter()
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"colors", ColorViewSet, basename="color")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"sizes", SizeViewSet, basename="size")
router.register(r"skus", SkuViewSet, basename="sku")
router.register(r"type", TypeViewSet, basename="type")

urlpatterns = [path("", include(router.urls))]
