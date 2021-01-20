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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def correct_password(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     if password1 != password2:
    #         raise ValidationError('Password do not match')
    #     return password2

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')

    #     if not email:
    #         raise ValidationError("Please enter your email address")
    #     return email

    # def same_username(self):
    #     username = self.cleaned_data.get('username')
    #     username_db = User.objects.get(username)

    #     if username == username_db:
    #         raise ValidationError("Chose enouther username")
    #     return username

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')

    #     if not username:
    #         raise ValidationError("Please enter your username")
    #     return username

    # def password_validation(self):
    #     if len(self) < 8:
    #         raise ValidationError("Password needs to have at least 8 signs.")
