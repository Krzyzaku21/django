from django.shortcuts import render
from articles.models import Article
from django.views import View
from django.core.paginator import Paginator
# Create your views here.


class LoadArticle(View):

    def get(self, request, article_id):
        context = {
            'article': Article.objects.get(id=article_id)
        }
        return render(request, 'article.html', context)


class LoadAllArticles(View):

    def get(self, request):
        context = {
            'articles_all': Article.objects.all()[::-1],
        }
        return render(request, 'articles_all.html', context)
