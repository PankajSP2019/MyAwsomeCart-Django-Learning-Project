from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    all_blog = Blogpost.objects.all()
    return render(request, 'blog/index.html', {'all_blog': all_blog})


def blogpost(request, pid):
    post = Blogpost.objects.filter(post_id=pid)[0]
    
    return render(request, "blog/blogpost.html", {'post': post})


def check(request):
    return HttpResponse("hello From Blog-Check")
