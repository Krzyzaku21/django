from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('login/', views.LoginPageView.as_view(), name='login'),
]
