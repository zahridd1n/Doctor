from django.db import models

class Vebinar(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.ImageField(upload_to="vebinar", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "vebinar"
        verbose_name_plural = "vebinars"


class VebinarRegister(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "vebinar register"
        verbose_name_plural = "vebinar registers"