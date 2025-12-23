from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class OurData(models.Model):
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "our data"
        verbose_name_plural = "our data"


class Socials(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    icon = models.ImageField(upload_to="socials", null=True, blank=True)
    