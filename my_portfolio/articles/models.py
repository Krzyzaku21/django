from django.db import models
from datetime import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title of Article')
    content = models.TextField(verbose_name='Content of Article')
    pub_date = models.DateTimeField(
        verbose_name='Date', default=datetime.now())
    article_image = models.ImageField(
        upload_to='image', verbose_name='Image of Article', null=True, blank=True)
