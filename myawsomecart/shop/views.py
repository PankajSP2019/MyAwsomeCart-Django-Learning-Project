from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/index.html')


def check(request):
    return HttpResponse("hello From Blog-Check")
