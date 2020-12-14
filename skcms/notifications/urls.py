from django.urls import path, include, re_path
from . import views
urlpatterns = [
    path('show/<int:notification_id>/', views.show_notification, name='show_notification'),
    path('delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
]