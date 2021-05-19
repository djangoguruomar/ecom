from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
import random
import string
from django.contrib.auth import authenticate,  login

def cartitem(request):

    if request.user.is_anonymous:
        letters = string.ascii_lowercase
        username="".join(random.choice(letters) for i in range(3))
        password=username
        print(username)
        user = User.objects.create_user(username=username, password=username, last_name="Guest")
        user = authenticate(username=username, password=password)
        login(request,user)
        
    user=request.user
    username=user.username
    customer, created= Customer.objects.get_or_create(user=user,name=username)
    order, created=Order.objects.get_or_create(customer=customer, complete=False)
    items=order.orderitem_set.all()
    products=Product.objects.all()
    
    context={'products': products, 'order': order, 'items': items, 'user':user}  
    return context

    