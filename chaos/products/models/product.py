from core.models import BaseModel
from django.db import models


class Product(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products"
    )
    type = models.ForeignKey("Type", on_delete=models.PROTECT, related_name="products")
    brand = models.ForeignKey("Brand", on_delete=models.PROTECT)

    class Meta(BaseModel.Meta):
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"
