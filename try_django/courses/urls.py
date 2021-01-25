from django.urls import path
from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

app_name = 'courses'
urlpatterns = [
    # path("", my_fbv, name='courses-list')
    path("", CourseView.as_view(template_name='contact.html'), name='courses-list'),
    path("<int:id>/", CourseView.as_view(), name='courses-detail'),
    path("courselist/", CourseListView.as_view(), name='courses-lists'),
    path("course1/", MyListView.as_view(), name='courses-lists-1'),
    path("create/", CourseCreateView.as_view(), name='courses-create'),
    path("<int:id>/update/", CourseUpdateView.as_view(), name='courses-update'),
    path("<int:id>/delete/", CourseDeleteView.as_view(), name='courses-delete'),
]
