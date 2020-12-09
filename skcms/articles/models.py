#-*- coding: utf-8 -*-
from django.db import models
# Create your models here.

#klasa artykułów
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Tytuł') #pole tekstowe z ciągiem znaków, parametry max_lenght -dł znaków, verbose_name - nazwa widoczna na zewnątrz
    content = models.TextField(verbose_name= 'Zawartość') #TextField - moze zawierac znacznie dłuższa liczbe znaków
    published = models.DateTimeField(verbose_name= 'Data publikacji') #DateTimeField - definicja daty
    image = models.FileField(upload_to='images', verbose_name='Obrazek') #pole przechowujace obrazki
    def __unicode__(self): #metoda odczytująca unicode na utf
        return self.title #rozpoznawanie po title

#klasa komentarze
class Comment(models.Model):
    name = models.CharField(max_length=150, verbose_name = 'Użytkownik')
    content = models.TextField(verbose_name= 'Komentarz')
    published = models.DateTimeField(verbose_name= 'Data publikacji')
    # relacja jeden do wielu przypisania komentarza do artykułu, ForeignKey - pole klucza obcego
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __unicode__(self): #metoda odczytująca unicode na utf
        return self.name #rozpoznawanie po name