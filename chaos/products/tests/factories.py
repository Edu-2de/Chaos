from factory.declarations import Sequence, SubFactory
from factory.django import DjangoModelFactory

from products.models import Brand, Category, Color, Product, Size, Sku, Type


class BrandFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Brand

    name = Sequence(lambda n: f"Brand {n}")


class CategoryFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Category

    name = Sequence(lambda n: f"Category {n}")


class ColorFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Color

    name = Sequence(lambda n: f"Color {n}")


class SizeFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Size

    name = Sequence(lambda n: f"Size {n}")


class TypeFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Type

    name = Sequence(lambda n: f"Type {n}")


class ProductFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Product

    name = Sequence(lambda n: f"Product {n}")
    description = "Description"
    category = SubFactory(CategoryFactory)
    type = SubFactory(TypeFactory)
    brand = SubFactory(BrandFactory)


class SkuFactory(DjangoModelFactory):
    class Meta:  # type:ignore
        model = Sku

    product = SubFactory(ProductFactory)
    color = SubFactory(ColorFactory)
    size = SubFactory(SizeFactory)
    price = "10.50"
    stock = 2
    barcode = Sequence(lambda n: f"{n:012d}")
