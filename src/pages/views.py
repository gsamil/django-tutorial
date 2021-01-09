from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request=request, template_name="home.html", context={})


def about_view(request, *args, **kwargs):
    # print(request.user)

    my_context = {
        "my_text": "This is my text.",
        "my_number": 10,
        "my_list": [1111, 2222, 3333, 'abcd'],
        "title": "this is a title",
        "my_html": "<h1>Hello World</h1>"
    }

    # return HttpResponse("<h1>Hello World</h1>")
    return render(request=request, template_name="about.html", context=my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
