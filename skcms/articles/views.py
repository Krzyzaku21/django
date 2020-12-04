from django.shortcuts import render #- zwroc zawartosc do przegladarki,
from articles.models import Article #- klasa z metodami odwołującymi się do bazy danych

# Create your views here.

def articles(request):
    return render(request, 'articles.html', {'articles' : Article.objects.all()}) #  Article.objects.all - pobieranie wszystkich danych z bazy i przypisanie ich do zmienniej articles

def article(request, article_id):
    return render(request, 'article.html', {'article' : Article.objects.get(id=article_id)})#  Article.objects.get - pobieranie danych id przypisanie ich do article_id do wyswietlania i do danych zmiennej article
