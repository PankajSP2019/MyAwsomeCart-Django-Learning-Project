from django.contrib import admin

# Register your models here.


# Adding/ Register Our Product Table to Admin shop/models -class name Product
from.models import Product, Contact, Order, OrderUpdate
# from .models import Contact

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
