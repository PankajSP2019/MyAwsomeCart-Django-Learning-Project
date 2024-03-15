from django.contrib import admin
from django.urls import path
from . import views  # import the views file

urlpatterns = [
    path("", views.index, name="blogIndex"),
    path("check/", views.check, name="blogCheck"),
    path("blogpost/<int:pid>", views.blogpost, name="blogPost")
]
