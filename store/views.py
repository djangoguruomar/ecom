from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import *
from .form import *
import json
from django.http import JsonResponse
from .utils import * 
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here

def store(request):
    context=cartitem(request)
    return render(request, 'store/home.html', context )

def cart(request):
    context=cartitem(request)
    return render(request, 'store/cart.html', context)

def checkout(request):
    context=cartitem(request)
    if request.method == "POST":
        
        form = ShippingForm(request.POST)

        if form.is_valid():
            instance=ShippingAddress()
            instance = form
            instance.save()
            orderprocess(request)
            return redirect('profile')
            
    else:
        customer=request.user.customer
        order=Order.objects.get(customer=customer, complete=False)
        form =  ShippingForm(initial={"customer": customer, "order":order})
    context["form"]=form
    return render(request, 'store/checkout.html', context)

def orderprocess(request):

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order.complete = True
    order.save()

    





def updateCart (request):
    

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print (str(order.id))
    orderItem, created = OrderItem.objects.get_or_create(order=order, products=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    if action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    if action == 'delete':
        orderItem.quantity =0
    print(orderItem.quantity)
    orderItem.save()
    return HttpResponse(json.dumps(orderItem.quantity), content_type='application/json',)


def admin_report(request):
    orders=Order.objects.all()
    items=OrderItem.objects.all()
    return render(request, 'store/myadmin.html', {'items': items, 'orders':orders})

def register(request):
    logout(request)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            username=username.capitalize()
            password= form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def profile(request):
    user=request.user
    username=user.username
    customer, created =Customer.objects.get_or_create(user=user, name=username)
    orders=Order.objects.all()
    items=OrderItem.objects.all()
    return render(request, 'store/profile.html',  {'orders':orders, 'items':items})
def change(request):
    context=cartitem(request)
    return render(request, 'store/update_cart.html', {'context':context})