#-*- coding: utf-8 -8-
from django.db import models

# Create your models here.

class Customhtml(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Tytuł')
    sourcehtml = models.TextField(verbose_name='Kod HTML')

    def __unicode__(self):
        return self.title