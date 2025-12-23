from .base import Base
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    service_price = models.TextField()


class ServicesDate(models.Model):
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "services date"
        verbose_name_plural = "services dates"


class Portfolio(models.Model):
    before_image = models.ImageField(upload_to="portfolio", null=True, blank=True)
    after_image = models.ImageField(upload_to="portfolio", null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"
