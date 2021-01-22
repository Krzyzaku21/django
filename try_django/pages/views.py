from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    # (<WSGIRequest: GET '/'>,) {} bez request, z request () {}
    print(args, kwargs)
    print(request.user)  # admin or AnonymousUser
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_title": "My title",
        "my_number": 123,
        "my_list": [123, 456, 789, "Abc"],
        "this_is_true": True,
        "my_code": "<h1>My Html</hq>"
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social World</h1>")  # string html code
    # (<WSGIRequest: GET '/'>,) {} bez request, z request () {}
    print(args, kwargs)
    print(request.user)  # admin or AnonymousUser
