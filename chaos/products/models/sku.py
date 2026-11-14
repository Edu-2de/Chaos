from core.models import BaseModel
from django.db import models
from django.db.models.expressions import F
from django.db.models.query_utils import Q


class Sku(BaseModel):
    product = models.ForeignKey(
        "Product", on_delete=models.PROTECT, related_name="skus"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotional_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock = models.PositiveIntegerField()
    barcode = models.CharField(max_length=15, unique=True)

    color = models.ForeignKey("Color", on_delete=models.PROTECT, related_name="skus")
    size = models.ForeignKey("Size", on_delete=models.PROTECT, related_name="skus")

    class Meta(BaseModel.Meta):
        verbose_name = "Sku"
        verbose_name_plural = "Sku's"
        constraints = (
            models.UniqueConstraint(
                name="sku-unique-product",
                fields=("product", "color", "size"),
                violation_error_message="This product already exists with this informations",
            ),
            models.CheckConstraint(
                name="sku_promotional_price_lower_than_price",
                condition=Q(promotional_price__isnull=True)
                | Q(promotional_price__lt=F("price")),
                violation_error_message="Promotional price cannot be greater than or equal to price",
            ),
            models.CheckConstraint(
                name="sku_product_min_value",
                condition=Q(price__gt=0),
                violation_error_message="Price must be greater than zero",
            ),
        )

    def __str__(self) -> str:
        return f"{self.product} - {self.color} - {self.size}"
