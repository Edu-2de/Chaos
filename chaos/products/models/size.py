from core.models import BaseModel
from django.db import models
from django.db.models.functions import Lower


class Size(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Size"
        verbose_name_plural = "Sizes"
        constraints = (
            models.UniqueConstraint(
                Lower("name"),
                name="size_unique_name",
                violation_error_message="This size already exists",
            ),
        )

    def __str__(self) -> str:
        return f"{self.name}"
