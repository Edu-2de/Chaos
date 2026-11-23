from django.urls import path

from .views import (
    BrandViewSet,
    BrandViewSetWithParams,
    CategoryViewSet,
    CategoryViewSetWithParams,
    ColorViewSet,
    ColorViewSetWithParams,
    ProductViewSet,
    ProductViewSetWithParams,
    SizeViewSet,
    SizeViewSetWithParams,
    SkuViewSet,
    SkuViewSetWithParams,
    TypeViewSet,
    TypeViewSetWithParams,
)

urlpatterns = [
    path("brands/", BrandViewSet.as_view(), name="brand-list"),
    path("brands/<int:pk>/", BrandViewSetWithParams.as_view(), name="brand-detail"),
    path("categories/", CategoryViewSet.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/",
        CategoryViewSetWithParams.as_view(),
        name="category-detail",
    ),
    path("colors/", ColorViewSet.as_view(), name="color-list"),
    path("colors/<int:pk>/", ColorViewSetWithParams.as_view(), name="color-detail"),
    path("products/", ProductViewSet.as_view(), name="product-list"),
    path(
        "products/<int:pk>/",
        ProductViewSetWithParams.as_view(),
        name="product-detail",
    ),
    path("sizes/", SizeViewSet.as_view(), name="size-list"),
    path("sizes/<int:pk>/", SizeViewSetWithParams.as_view(), name="size-detail"),
    path("skus/", SkuViewSet.as_view(), name="sku-list"),
    path("skus/<int:pk>/", SkuViewSetWithParams.as_view(), name="sku-detail"),
    path("type/", TypeViewSet.as_view(), name="type-list"),
    path("type/<int:pk>/", TypeViewSetWithParams.as_view(), name="type-detail"),
]
