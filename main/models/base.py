from django.db import models


class Base(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


    class Meta:
        verbose_name = "base"
        verbose_name_plural = "base"