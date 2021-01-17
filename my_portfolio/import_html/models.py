# -*-- coding: utf-8 -8-
from django.db import models

# Create your models here.


class ImportHtml(models.Model):
    title = models.CharField(max_length=150, verbose_name='Name html file')
    sourcehtml = models.TextField(verbose_name="HTML CODE")

    def __unicode__(self):
        return self.title
