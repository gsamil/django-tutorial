from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'title': 'I set this title as initial value'
    }
    # form = RawProductForm(request.POST or None, initial=initial_data)
    # We can use model form instead of Django form
    obj = Product.objects.get(id=2)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view_form(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view_raw_html(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        print(title)
        # Product.objects.create(title=title)
    context = {}
    return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
