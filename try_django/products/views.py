from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def product_list_view(request):
    # queryset - zestaw zapytań dla pobrania listy
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset,
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        # confirm delete
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj,
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    print(Product)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj,
    }
    return render(request, "products/dynamic_lookup.html", context)


def product_initial_data(request):
    initial_data = {
        'title': "my awesome title"
    }
    obj = Product.objects.get(id=13)
    #    initial=initial_data, # pole tekstowe wypełnione, instance - zczytana instancja z bazy danych
    form = ProductForm(request.POST or None, instance=obj,)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, "products/product_initial.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # data is good now
#             # {'title': 'ewrw', 'description': 'wer', 'price': Decimal('32432.56')}
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form,
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     # <QueryDict: {}> dla adressu "http://127.0.0.1:8000/create/?title=aaa" <QueryDict: {'title': ['aaa']}>
#     print(request.GET)
#     # < klucz pozycji dla adressu "http://127.0.0.1:8000/create/?title=aaa" aaa
#     # print(request.GET['title']) - nie używać brak bezpieczeństwa
#     # <QueryDict: {'csrfmiddlewaretoken': ['xANcQxHQYtpHDsBZ67xEvtorXCxoEqrsh84JHwmQBotEMXSyDdi268uZJwp6z1GH'], 'title': ['abc']}>
#     print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)  # abc
#     # Product.objects.create(title=title)
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = ProductForm() by czyścić formularz po zapisaniu
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # obj = Product.objects.get(id=10)
    # context = {
    #     "title": obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)
