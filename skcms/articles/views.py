from django.shortcuts import render #- zwroc zawartosc do przegladarki,
from articles.models import Article, Comment #- klasa z metodami odwołującymi się do bazy danych
from articles.forms import CommentForm #klasa formularza za komentarze
from django.template.context_processors import csrf
from django.utils import timezone #data publikacji automatycznie
from django.http import HttpResponseRedirect #klasa która umożliwia dodanie przekierowania HTTP

# Create your views here.
def articles(request):
    return render(request, 'articles.html', {'articles' : Article.objects.all()}) #  Article.objects.all - pobieranie wszystkich danych z bazy i przypisanie ich do zmienniej articles

def article(request, article_id):
    return render(request, 'article.html', {'article' : Article.objects.get(id=article_id)})#  Article.objects.get - pobieranie danych id przypisanie ich do article_id do wyswietlania i do danych zmiennej article

def add_comment(request,article_id):
	art = Article.objects.get(id=article_id)

	if request.method == "POST":
		cf = CommentForm(request.POST)
		if cf.is_valid():
			comment = cf.save(commit=False)
			comment.published = timezone.now()
			comment.article = art
			comment.save()

			return HttpResponseRedirect('/article/%s' % article_id)

	else:
		cf = CommentForm()

	args = {}
	args.update(csrf(request))
	args['article'] = art
	args['form'] = cf

	return render(request, 'add_comment.html', args)
