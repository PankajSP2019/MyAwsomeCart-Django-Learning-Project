from django.shortcuts import render
from django.http import HttpResponse
# Import Product from Model
from .models import Product
from math import ceil


def index(request):
    # products = Product.objects.all() # Fetch all the Product
    allProds = []
    category_and_id = Product.objects.values('category', 'id')  # It will fetch all the category and id column's data
    all_category = {item['category'] for item in category_and_id}  # Set comprehensions for store the unique category name
    for category in all_category:
        prod = Product.objects.filter(category=category)  # Fetch item details based on category
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        # Store the data based on category in the main list
        allProds.append([prod, range(1, nSlides), nSlides])

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
