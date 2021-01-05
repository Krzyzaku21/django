from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import auth  # system uwierzytelnienia i autoryzacji użytkownika
from django.template.context_processors import csrf  # generator unikallnego tokena
# formularz tworzenia nowego użytkownika
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')
