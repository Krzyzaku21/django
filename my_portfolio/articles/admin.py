from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

admin.site.register(models.Comment, MPTTModelAdmin)

admin.site.register(models.Article)


# @admin.register(models.Post)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'status')
