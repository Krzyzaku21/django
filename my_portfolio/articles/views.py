from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
from .models import Article, Comment
from .forms import ArticleModelForm, NewCommentForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from social_django.models import UserSocialAuth
# Create your views here.


class LoadArticle(View):

    def get(self, request, article_id):

        post = get_object_or_404(Article, id=article_id, status='published')
        allcomments = post.comments.filter(status=True)
        page = request.GET.get('page', 1)

        paginator = Paginator(allcomments, 10)
        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            comments = paginator.page(1)
        except EmptyPage:
            comments = paginator.page(paginator.num_pages)

        else:
            comment_form = NewCommentForm()
            context = {
                'article': Article.objects.get(id=article_id),
                'post': post, 'comments': comments, 'comment_form': comment_form, 'allcomments': allcomments,
                'auth_social_users_fb': UserSocialAuth.objects.filter(provider='facebook').values_list(
                    'user_id', flat=True),
                'auth_social_users_git': UserSocialAuth.objects.filter(provider='github').values_list(
                    'user_id', flat=True),
                'auth_social_users_uid': UserSocialAuth.objects.filter().values_list(
                    'uid', flat=True)
            }
        return render(request, 'article.html', context)

    def post(self, request, article_id):
        post = get_object_or_404(Article, id=article_id, status='published')
        user_comment = None
        if request.method == 'POST':
            comment_form = NewCommentForm(request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                user_comment.post = post
                user_comment.user = request.user
                user_comment.save()
                return HttpResponseRedirect('../' + str(article_id))


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
                    form_class.instance.article_author_id = request.user.id
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
