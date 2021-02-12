from django import forms
from django.forms.widgets import DateTimeInput, Textarea
from .models import Article, Comment
from datetime import date, datetime
from mptt.forms import TreeNodeChoiceField
from django.contrib.auth.models import User


class ArticleModelForm(forms.ModelForm):  # widok tworzenia lub aktualizacji formularza
    class Meta:
        model = Article
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        fields = ['title', 'content', 'article_image']
        widgets = {
            'pub_date': DateTimeInput(
                attrs={
                    'template_name': 'django/forms/widgets/datetime.html',
                    'type': 'datetime-local',
                    'min': f"{date.today()}T{current_time}",
                    'max': f"{date.today()}T{current_time}",
                }),
            'content': Textarea(
                attrs={
                    'template_name': 'django/forms/widgets/textarea.html',
                    'rows': 10,
                    'width': '100%',
                    'cols': '100%',
                    'style': 'width: 100%;',
                }
            ),
        }


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        model2 = Article
        fields = ('content', 'parent')

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 98%; margin: auto; padding: 5px; align-items: center;',
                'rows': 10,
            }),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)
