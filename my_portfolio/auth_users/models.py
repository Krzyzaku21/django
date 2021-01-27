from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        max_length=8, verbose_name="date of birth")
    image_add = models.ImageField(
        upload_to="avatars", verbose_name="avatar")

    def __str__(self):
        return self.user.username
