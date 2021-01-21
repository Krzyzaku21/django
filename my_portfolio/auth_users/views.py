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


class LoaderHomePage(View):
    def get(self, request):
        article_list = Article.objects.all()[::-1]
        page_number = request.GET.get('page')
        article_paginator = Paginator(article_list, 5)
        page_obj = article_paginator.get_page(page_number)

        register_obj = Register.objects.all()

        context = {
            'page_obj': page_obj,
            'register_obj': register_obj,
        }
        return render(request, 'base.html', context)

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True
        if password == '':
            messages.add_message(request, messages.ERROR,
                                 'Password is required')
            context['has_error'] = True
        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'login.html', status=401, context=context)
        login(request, user)
        return redirect('/')


class LoginPageView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True
        if password == '':
            messages.add_message(request, messages.ERROR,
                                 'Password is required')
            context['has_error'] = True
        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'login.html', status=401, context=context)
        login(request, user)
        return redirect('/')


class LogoutPageView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterPageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('base.html')
        user_form = CreateUserForm(request.POST)
        register_form = RegisterForm(request.POST)
        context = {'user_form': user_form, 'register_form': register_form}
        return render(request, 'register.html', context)

    def post(self, request):
        if request.method == 'POST':
            register_form = RegisterForm(request.POST, request.FILES)
            image_adds = request.FILES.get('image_add')
            register_form.instance.image_add = image_adds
            height_image = register_form.instance.image_add.height
            width_image = register_form.instance.image_add.width
            if height_image < 250 and width_image < 250:
                user_form = CreateUserForm(request.POST)
                if user_form.is_valid():
                    user_form.save()
                    user_form_id = user_form.instance.id
                    register_form.instance.image_add = image_adds
                    register_form.instance.user_id = user_form_id
                    if register_form.is_valid():
                        register_form.save()
                    user = user_form.cleaned_data.get('username')
                    messages.success(
                        request, 'Your account has been registered' + user)
                    return redirect('login')
            if height_image > 250 and width_image > 250:
                user_form = CreateUserForm(request.POST)
                user_form.full_clean()
                messages.error(request, "your photo need to be 250px/250px")
            else:
                print(user_form.errors)
        context = {'user_form': user_form, 'register_form': register_form}
        return render(request, 'register.html', context)
