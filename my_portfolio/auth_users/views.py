from email.mime.image import MIMEImage
from email.mime.text import MIMEText  # Added
from email.mime.multipart import MIMEMultipart
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
from django.views.generic import TemplateView

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
UserModel = get_user_model()


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
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            user_form = CreateUserForm(request.POST)
            register_form = RegisterForm(request.POST)
        context = {'user_form': user_form, 'register_form': register_form}
        return render(request, self.template_name, context)

    def image_email(self):
        static_image = 'my_portfolio\static\img\LOGO150x40.png'

    def post(self, request):
        if request.method == 'POST':
            user_form = CreateUserForm(request.POST)
            register_form = RegisterForm(request.POST, request.FILES)
            if user_form.is_valid():
                user = user_form.save()
                user_form_id = user_form.instance.id
                register_form.instance.user_id = user_form_id
                if register_form.is_valid():
                    register_form.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    username = user_form.cleaned_data.get('username')
                    message = render_to_string('active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    })
                    to_email = user_form.cleaned_data.get('email')
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return HttpResponse('Please confirm your email address to complete the registration')
            else:
                print(f"Error like: {user_form.errors}")
                print(f"Error like: {register_form.errors}")
        else:
            context = {'user_form': user_form, 'register_form': register_form}
            return render(request, self.template_name, context)


class RegisterActivateView(View):
    def post(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


class RegisterAsk(View):
    template_name = 'register_ask.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class RegisterConfirm(View):
    template_name = 'register_confirm.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


# class RegisterPageView(View):
#     template_name = 'register.html'

#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('/')
#         else:
#             user_form = CreateUserForm(request.POST)
#             register_form = RegisterForm(request.POST)
#         context = {'user_form': user_form, 'register_form': register_form}
#         return render(request, self.template_name, context)

#     def post(self, request):
#         if request.method == 'POST':
#             user_form = CreateUserForm(request.POST)
#             register_form = RegisterForm(request.POST, request.FILES)
#             if user_form.is_valid():
#                 user = user_form.save()
#                 user_form_id = user_form.instance.id
#                 register_form.instance.user_id = user_form_id
#                 if register_form.is_valid():
#                     register_form.save()
#                     username = user_form.cleaned_data.get('username')
#                     messages.success(request, 'Account was created for ' + username)
#                     return redirect('login')
#             else:
#                 print(f"Error like: {user_form.errors}")
#                 print(f"Error like: {register_form.errors}")

#         context = {'user_form': user_form, 'register_form': register_form}
#         return render(request, self.template_name, context)
