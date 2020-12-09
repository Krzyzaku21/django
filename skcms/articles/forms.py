from django import forms
from .models import Comment

#klasa formularzy
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'content') #powiązanie - formularz edycji komentarza.