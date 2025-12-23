from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.DateField()
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "registration"
        verbose_name_plural = "registrations"
