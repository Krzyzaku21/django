from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoaderHomePage.as_view(), name='base'),
]
