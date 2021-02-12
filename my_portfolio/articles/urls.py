from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_id>/', views.LoadArticle.as_view(), name='article-id'),
    path('all/', views.LoadAllArticles.as_view()),
    path('create/', views.CreateArticle.as_view(), name='article-create'),
]
