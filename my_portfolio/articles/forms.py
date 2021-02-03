from django import forms
from django.forms.widgets import DateTimeInput
from .models import Article
from datetime import date


class ArticleModelForm(forms.ModelForm):  # widok tworzenia lub aktualizacji formularza
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'pub_date': DateTimeInput(
                attrs={
                    'template_name': 'django/forms/widgets/datetime.html',
                    'type': 'datetime-local',
                    'min': "1914-05-11T00:00",
                    'max': f"{date.today()}T23:59",
                })
        }
