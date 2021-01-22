from django import forms
from django.forms.widgets import DateInput
from django.forms import ModelForm
from .models import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['date_of_birth', 'image_add']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

    def image_size(self):
        image_height = self.image_add.height
        image_width = self.image_add.width
        if image_height > 250 and image_width > 250:
            raise ValidationError("your photo need to be 250px/250px")
        else:
            return self.image_add


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
