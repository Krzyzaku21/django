from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

admin.site.register(models.Comment, MPTTModelAdmin)

admin.site.register(models.Article)
