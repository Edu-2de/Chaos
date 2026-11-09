from core.models import BaseModel
from django.db import models
from django.db.models.functions import Lower


class Color(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Color"
        verbose_name_plural = "Colors"
        constraints = (
            models.UniqueConstraint(
                Lower("name"),
                name="color_unique_name",
                violation_error_message="This color already exits",
            ),
        )

    def __str__(self) -> str:
        return f"{self.name}"
