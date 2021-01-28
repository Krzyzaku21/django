from django.db import models
from django.contrib.auth.models import User
from .validators import validate_image, no_future_date


class Register(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        max_length=8, verbose_name="date of birth", validators=[no_future_date])
    image_add = models.ImageField(
        upload_to="avatars", verbose_name="avatar", validators=[validate_image])

    def __str__(self):
        return self.user.username
