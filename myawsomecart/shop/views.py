from django.shortcuts import render
from django.http import HttpResponse
# Import Product from Model
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    allProds = [[products, range(1, nSlides), nSlides],
                [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def check(request):
    return HttpResponse("hello From Blog-Check")


# Pipeline For Shop
def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/contact.html')


def tracker(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/tracker.html')


def search(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/search.html')


def productview(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/productview.html')


def checkout(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/checkout.html')
