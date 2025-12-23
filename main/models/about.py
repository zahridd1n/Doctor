from .base import Base
from django.db import models

class Advantages(models.Model):
    icon = models.ImageField(upload_to="advantages", null=True, blank=True)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "advantage"
        verbose_name_plural = "advantages"

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="about", null=True, blank=True)
    signature = models.ImageField(upload_to="about", null=True, blank=True)