from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from auth_users.forms import RegisterForm, CreateUserForm
from django.contrib import messages
from django.core.paginator import Paginator
from articles.models import Article
from auth_users.models import Register

# Create your views here.


class BaseArticlesView(object):

    def get_articles_ten(self, request):
        article_list = Article.objects.all()[::-1]
        page_number = request.GET.get('page')
        article_paginator = Paginator(article_list, 10)
        page_obj = article_paginator.get_page(page_number)
        return page_obj


class BaseRegister(object):

    def get_register(self):
        reg_obj = Register.objects.all()
        return reg_obj


class BaseLoginView(object):

    def post_login(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
        return user

#! central GET-------------------------------------


class LoaderHomePage(BaseArticlesView, View, BaseLoginView, BaseRegister):

    def get(self, request):
        context = {
            'page_obj': self.get_articles_ten(request),
            'reg_obj': self.get_register,
        }
        return render(request, 'base.html', context)
#! central POST-------------------------------------

    def post(self, request):

        if self.post_login(request) is not None:
            login(request, self.post_login(request))
            return redirect('base')
        else:
            messages.info(request, "Incorrect username or password")
            return redirect('base')
        context = {}
        return render(request, 'base.html', context)
#!--------------------------------------------------
