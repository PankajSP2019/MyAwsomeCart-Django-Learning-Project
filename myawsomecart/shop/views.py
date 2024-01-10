from django.shortcuts import render
from django.http import HttpResponse
# Import Product from Model
from .models import Product


def index(request):
    products = Product.objects.all()
    # return HttpResponse("hello From Blog-Index")
    print(products)
    return render(request, 'shop/index.html',{'product':products})


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
