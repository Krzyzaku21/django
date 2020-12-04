from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('show_all/', views.articles, name='articles'),
    path('<int:article_id>/', views.article, name='article'),
]