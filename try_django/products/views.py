from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.


def product_create_view(request):
    # <QueryDict: {}> dla adressu "http://127.0.0.1:8000/create/?title=aaa" <QueryDict: {'title': ['aaa']}>
    print(request.GET)
    # < klucz pozycji dla adressu "http://127.0.0.1:8000/create/?title=aaa" aaa
    # print(request.GET['title']) - nie używać brak bezpieczeństwa
    # <QueryDict: {'csrfmiddlewaretoken': ['xANcQxHQYtpHDsBZ67xEvtorXCxoEqrsh84JHwmQBotEMXSyDdi268uZJwp6z1GH'], 'title': ['abc']}>
    print(request.POST)
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        print(my_new_title)  # abc
    # Product.objects.create(title=title)
    context = {}
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         # form = ProductForm() by czyścić formularz po zapisaniu
#         form = ProductForm()
#     context = {
#         'form': form,
#     }
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)
