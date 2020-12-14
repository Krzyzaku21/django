from django import forms
from .models import UserProfile

#klasa definiująca pola w formularzu
class UserProfileForm(forms.ModelForm):
#klasa Meta definiująca metadane
    class Meta:
        model = UserProfile
        fields = ('country', 'age') # fields - pola do edycji
