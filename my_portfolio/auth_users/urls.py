from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('register/confirm/', views.RegisterConfirm.as_view(), name='register-confirm'),
    path('register/login/', views.RegisterLog.as_view(), name='register-log'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
