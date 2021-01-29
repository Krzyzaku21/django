from django import forms
from django.forms.widgets import DateInput
from django.forms import ModelForm
from .models import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['date_of_birth', 'image_add']
        widgets = {
            'date_of_birth': DateInput(
                attrs={
                    'class': 'datepicker',
                    'type': 'date',
                    'min': "1914-05-11",
                    'max': date.today() - relativedelta(years=18),
                })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
