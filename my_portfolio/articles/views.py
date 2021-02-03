from django.shortcuts import render, redirect
from django.http import HttpResponse
from articles.models import Article
from django.views import View
from django.core.paginator import Paginator
from auth_users.models import Register
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm
# Create your views here.


class LoadArticle(View):

    def get(self, request, article_id):
        context = {
            'article': Article.objects.get(id=article_id),
        }
        return render(request, 'article.html', context)


class CreateArticle(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form_class = ArticleModelForm(request.POST, request.FILES)
            context = {
                'form_class': form_class,
            }
            return render(request, 'create_article.html', context)
        else:
            return redirect('/')

    def post(self, request):
        if request.method == 'POST':
            if request.user.is_authenticated:
                form_class = ArticleModelForm(request.POST, request.FILES)
                if form_class.is_valid():
                    form_class.save()
                context = {
                    'form_class': form_class,
                }
                return redirect('base')
            else:
                return HttpResponse('Page dont exist please login')


class LoadAllArticles(View):

    def get(self, request):
        context = {
            'articles_all': Article.objects.all()[::-1],
        }
        return render(request, 'articles_all.html', context)
