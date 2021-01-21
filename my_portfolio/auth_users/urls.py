from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoaderHomePage.as_view(), name='base'),
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
]
