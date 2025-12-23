from django.db import models


class Base(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = "base"
        verbose_name_plural = "base"