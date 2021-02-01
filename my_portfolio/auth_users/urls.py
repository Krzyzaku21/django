from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('register/ask/', views.RegisterAsk.as_view(), name='register-ask'),
    path('register/confirm/', views.RegisterConfirm.as_view(), name='register-confirm'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', views.RegisterActivateView.as_view(), name='activate'),
]
