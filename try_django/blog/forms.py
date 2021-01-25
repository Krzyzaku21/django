from django import forms

from .models import Article


class ArticleModelForm(forms.ModelForm):  # widok tworzenia lub aktualizacji formularza
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]
