"""skcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from skcms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('articles.urls')),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/auth/', views.auth_view, name='auth_view'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/loggedin/', views.loggedin, name='loggedin'),
    path('accounts/invalid/', views.invalid_login, name='invalid_login'),
    path('accounts/create_user/', views.create_user, name='create_user'),
    path('accounts/create_user_success/', views.create_user_success, name='create_user_success'),

]
#Do ładowania zdjęć w trybie DEBUG oraz CSS
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
