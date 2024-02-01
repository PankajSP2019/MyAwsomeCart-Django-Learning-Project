import json

from django.shortcuts import render, redirect  # Import redirect to redirect the page
from django.contrib import messages  # For showing up the messages
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate  # Import Product, Contact, Order, OrderUpdate from Model
from django.contrib import messages  # For using the message library
from django.shortcuts import render, redirect  # For using render,  redirect
from math import ceil


def index(request):
    # products = Product.objects.all() # Fetch all the Product
    allProds = []
    category_and_id = Product.objects.values('category', 'id')  # It will fetch all the category and id column's data
    all_category = {item['category'] for item in
                    category_and_id}  # Set comprehensions for store the unique category name
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
    if request.method == "POST":
        # Here I will add an condition that, no field will not be empty
        # Ex : if name != ""
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        contact_d = Contact(name=name, email=email, phone=phone, desc=desc)
        contact_d.save()
        # Add a success message using Django's messaging framework
        messages.success(request, "You successfully dropped your message. We will contact you soon.")
        # It will redirect
        return redirect('/shop/contact')

    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == 'POST':
        # Here I will add an condition that, no field will not be empty
        # Ex : if name != ""
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def search(request):
    # return HttpResponse("hello From Blog-Index")
    return render(request, 'shop/search.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)  # based on id fetch the product details
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        # Here I will add an condition that, no field will not be empty
        # Ex : if name != ""
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')

        order = Order(items_json=items_json, name=name, phone=phone,
                      email=email, address=address, city=city, state=state, zip_code=zip_code)
        order.save()

        # Also Insert the data in the OrderUpdate Table, the purpose of this, to track the order
        update = OrderUpdate(order_id=order.order_id, update_desc="The Order Has Been Placed.")
        update.save()

        # For passing the Message
        thank = True
        oid = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': oid})

    return render(request, 'shop/checkout.html')
