from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import auth #system uwierzytelnienia i autoryzacji użytkownika
from django.template.context_processors import csrf #generator unikallnego tokena

class Login(View):
    def get(self, request):
        context = {} # c - element przechowujący argumenty
        context.update(csrf(request))
        return render(request, 'login.html', context)

def auth_view(request):
    context = {}
    return render(request, 'auth_view.html', context)


