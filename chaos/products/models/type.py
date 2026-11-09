from core.models import BaseModel
from django.db import models
from django.db.models.functions import Lower


class Type(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Type"
        verbose_name_plural = "Types"
        constraints = (
            models.UniqueConstraint(
                Lower("name"),
                name="type_unique_name",
                violation_error_message="This type already exists",
            ),
        )

    def __str__(self) -> str:
        return f"{self.name}"
