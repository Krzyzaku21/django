# from django.shortcuts import render, redirect
# from django.views import View
# from django.http import HttpResponseRedirect
# from django.contrib import auth
# from django.template.context_processors import csrf
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .forms import RegisterForm
# from django.contrib import messages
# from notifications.models import Notifications


# class RegisterPageView(View):

#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('/')
#         form = UserCreationForm()
#         return render(request, 'register.html', {'form': form})

#     def post(self, request):
#         if request.method == 'POST':
#             user_form = UserCreationForm(request.POST)
#             register_form = RegisterForm(request.POST)
#             if user_form.is_valid() and register_form.is_valid():
#                 username = user_form.cleaned_data['username']
#                 email = user_form.cleaned_data['email']
#                 try:
#                     user = User.objects.get(
#                         username=user_form.cleaned_data['username'])
#                     context = {'user_form': user_form,
#                                'error': 'This username has taken'}
#                     return render(request, 'register.html', context)
#                 except User.DoesNotExist:
#                     args = {}
#                     args.update(csrf(request))
#                     args['form'] = UserCreationForm()
#                 try:
#                     email = User.objects.get(
#                         email=user_form.cleaned_data['email'])
#                     context = {'user_form': user_form,
#                                'error': 'This email has been used'}
#                     return render(request, 'register.html', context)
#                 except User.DoesNotExist:
#                     args = {}
#                     args.update(csrf(request))
#                     args['user_form'] = UserCreationForm()
#             else:
#                 user_form = UserCreationForm()
#                 register_form = RegisterForm()
#             return render(request, 'register.html', {'user_form': user_form, 'register_form': register_form})


# class LoginPageView(View):

#     def get(self, request):
#         context = {}
#         context.update(csrf(request))
#         return render(request, 'login.html', context)


# class AuthView(View):

#     def auth_view(self, request):
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return HttpResponseRedirect('/accounts/loggedin/')
#         else:
#             return HttpResponseRedirect('/accounts/invalid/')


# class LoggedinPageView(View):

#     def loggedin(self, request):
#         n = Notifications.objects.filter(user=request.user, viewed=False)
#         return render(request, 'loggedin.html', {'user_name': request.user.username, 'notification': n})


# class LogoutPageView(View):

#     def logout(self, request):
#         auth.logout(request)
#         return render(request, 'logout.html')


# class InvalidLoginPageView(View):

#     def invalid_login(self, request):
#         return render(request, 'invalid_login.html')
