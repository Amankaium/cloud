from django.db import models

# Create your models here.
class Order(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    date_create = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    date_update = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.email
