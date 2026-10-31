from core.models import BaseModel
from django.db import models


class Type(BaseModel):
    name = models.CharField(max_length=30)

    class Meta(BaseModel.Meta):
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self) -> str:
        return f"{self.name}"
