from core.models import BaseModel
from django.db import models


class Color(BaseModel):
    name = models.CharField(max_length=30, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self) -> str:
        return f"{self.name}"
