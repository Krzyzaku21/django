from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.


class Article(models.Model):
    class ArticleManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200, verbose_name='Title of Article')
    content = models.TextField(verbose_name='Content of Article')
    pub_date = models.DateTimeField(verbose_name='Date', default=datetime.now, editable=False)
    article_image = models.ImageField(upload_to='image', verbose_name='Image of Article', null=True, blank=True)
    article_author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    articlemanager = ArticleManager()  # custom manager

    class MPTTMeta:
        order_by = ('-publish')

        def __str__(self):
            return self.title


class Comment(MPTTModel):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.content
