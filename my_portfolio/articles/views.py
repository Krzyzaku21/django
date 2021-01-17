from django.shortcuts import render
from articles.models import Article
from django.views import View
from django.core.paginator import Paginator
# Create your views here.


class LoadArticles(View):

    def get(self, request):
        article_list = Article.objects.all()[::-1]
        page_number = request.GET.get('page')
        article_paginator = Paginator(article_list, 5)
        page_obj = article_paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'articles.html', context)


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
