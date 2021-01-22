from django.db import models

# Create your models here.

# https://docs.djangoproject.com/pl/3.1/ref/models/fields/#field-types


class Product(models.Model):
    title = models.CharField(max_length=120)
    # blank - wymagane do wypełnienia , null - wartosc moze byc pusta
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField()
    features = models.BooleanField(default=True)  # null=True, default=True
