from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
# from notifications.models import Notifications


class LoginPageView(View):

    def get(self, request):
        context = {}
        context.update(csrf(request))
        return render(request, 'login.html', context)


class AuthView(View):

    def auth_view(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/loggedin/')
        else:
            return HttpResponseRedirect('/accounts/invalid/')


# class LoggedinPageView(View):

#     def loggedin(self, request):
#         n = Notifications.objects.filter(user=request.user, viewed=False)
#         return render(request, 'loggedin.html', {'user_name': request.user.username, 'notification': n})


class LogoutPageView(View):

    def logout(self, request):
        auth.logout(request)
        return render(request, 'logout.html')


class InvalidLoginPageView(View):

    def invalid_login(self, request):
        return render(request, 'invalid_login.html')
