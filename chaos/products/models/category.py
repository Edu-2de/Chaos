from core.models import BaseModel
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        constraints = (
            models.UniqueConstraint(
                name="category_unique_name",
                fields=("name"),
                violation_error_message="This category already exists",
            ),
        )

    def __str__(self) -> str:
        return f"{self.name}"
