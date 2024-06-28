from rest_framework import serializers 

from cart.models import Cart,CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id','cart','product','quantity','price']

class CartSerializer(serializers.ModelSerializer):
    cartItem = CartItemSerializer(many =True,read_only=True)
    class Meta:
        model = Cart
        fields =['user','total_amount','cartItem','total_items','created']
