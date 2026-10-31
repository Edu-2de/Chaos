from core.models import BaseModel
from django.db import models


class Size(BaseModel):
    name = models.CharField(max_length=30, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self) -> str:
        return f"{self.name}"
