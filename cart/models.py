from django.db import models
from django.contrib.auth.models import User

from Store.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField(default =0)
    total_items = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "   " + str(self.total_amount)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartItem')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price =  models.IntegerField()

    def __str__(self):
        return self.cart.user.username + "   " + self.product.name
