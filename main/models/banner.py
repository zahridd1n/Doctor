from .base import Base
from django.db import models


class Banner(Base):
    image = models.ImageField(upload_to="banner", null=True, blank=True)

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "banners"

    def __str__(self):
        return self.title

