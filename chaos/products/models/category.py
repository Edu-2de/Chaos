from core.models import BaseModel
from django.db import models
from django.db.models.functions import Lower


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        constraints = (
            models.UniqueConstraint(
                Lower("name"),
                name="category_unique_name",
                violation_error_message="This category already exists",
            ),
        )

    def __str__(self) -> str:
        return f"{self.name}"
