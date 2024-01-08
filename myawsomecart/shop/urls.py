from django.contrib import admin
from django.urls import path
from . import views  # import the views file

urlpatterns = [
    path("", views.index, name="shopIndex"),
    path("check/", views.check, name="shopCheck"),  # Just for check
    path("about/", views.about, name="AboutUS"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productview, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
