from django.contrib import admin
from django.urls import path
from . import views  # import the views file

urlpatterns = [
    path("", views.index, name="shopIndex"),
    path("check/", views.check, name="shopCheck")
]
