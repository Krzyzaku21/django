#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #Sygnały zdarzenia
from django.dispatch import receiver #Odbiornik sygnału zdarzenia
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #relacja 1 do 1 powiązania kąta użytkownika
    country = models.CharField(max_length=200, verbose_name='Kraj')
    age = models.CharField(max_length=3, verbose_name='Wiek')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0]) #pobieramy albo tworzymy użytkownika w właściwosci profile funkcja get_or_create

#Utworzony nowy rekord w tabeli użytkownicy auth_users
@receiver(post_save, sender=User)
def add_user_profile_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfile.objects.create(user=kwargs.get('instance')) #utworzenie automatycznie nowego rekordu w tabeli z user_profile