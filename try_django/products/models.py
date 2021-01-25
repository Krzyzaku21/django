from django.db import models
from django.urls import reverse
# Create your models here.

# https://docs.djangoproject.com/pl/3.1/ref/models/fields/#field-types


class Product(models.Model):
    title = models.CharField(max_length=120)
    # blank - wymagane do wypełnienia , null - wartosc moze byc pusta
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField()
    features = models.BooleanField(default=True)  # null=True, default=True

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/"

    def get_absolute_url(self):
        # na podstawie urls
        return reverse("products:product-detail", kwargs={"my_id": self.id})
