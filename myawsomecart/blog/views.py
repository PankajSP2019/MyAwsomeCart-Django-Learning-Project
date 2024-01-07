from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("hello From Blog-Index")


def check(request):
    return HttpResponse("hello From Blog-Check")
