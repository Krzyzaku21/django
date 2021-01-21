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
        image = self.cleaned_data.get('image_add')
        if image.height > 250 and image.width > 250:
            raise ValidationError("your photo need to be 250px/250px")
        else:
            return image


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
