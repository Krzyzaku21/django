from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.LoadArticles.as_view()),
    path('articles/<int:article_id>/', views.LoadArticle.as_view()),
    path('articles/all/', views.LoadAllArticles.as_view()),
]
