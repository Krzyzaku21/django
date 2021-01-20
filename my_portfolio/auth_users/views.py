from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from auth_users.forms import RegisterForm, CreateUserForm
from django.contrib import messages


class RegisterPageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
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
        # else:
        #     return redirect('register')


class LoginPageView(View):

    def get(self, request):
        context = {}
        return render(request, 'login.html', context)

    # def get(self, request):
    #     if request.user.is_authenticated:
    #         return redirect('/')

    # def post(self, request):
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')

    #         user = authenticate(request, username=username, password=password)

    #         if user is not None:
    #             login(request, user)
    #             return redirect('/')
    #         else:
    #             messages.info(request, 'Username OR password is incorrect')
    #     context = {}
    #     return render(request, 'login.html', context)
