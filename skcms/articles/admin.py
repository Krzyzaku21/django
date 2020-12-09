from django.contrib import admin
from articles.models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
