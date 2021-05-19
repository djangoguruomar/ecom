from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField (max_length=50, null=True)
    guest = models.BooleanField(default=False)



    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField (max_length=50)
    price=models.DecimalField( max_digits=5, decimal_places=2)
    image=models.ImageField( null=True, blank=True)

    def __str__(self):
        return self.name    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def grand_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def cart_total_item(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
        




    


class OrderItem (models.Model):
    products=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.products.price*self.quantity 
        print(total)
        return total


    
class ShippingAddress(models.Model):
    name = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.address
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'