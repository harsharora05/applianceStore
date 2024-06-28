from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView,Response

from Store.models import Product
from cart.models import Cart,CartItem
from cart.api.serializer import CartSerializer,CartItemSerializer


# Create your views here.

class CartView(APIView):

    def get(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)



class AddToCartView(APIView):

    def post(self,request,pk):
        user = request.user
        cart ,created = Cart.objects.get_or_create(user = user)
        product = get_object_or_404(Product, id=pk)
        product_price = product.price
        ordered_quantity = request.data['quantity']

        data = {'cart': cart.id, 'product': product.id,'quantity': ordered_quantity, 'price': product_price}
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            total_cart_price = int(ordered_quantity) * product_price
            cart.total_items = cart.total_items +int(ordered_quantity)
            cart.total_amount  += total_cart_price
            cart.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class UpdateCartView(APIView):
    def put(self,request,pk):
        cart = Cart.objects.get(user = request.user)
        cartItem = get_object_or_404(CartItem,id = pk)
        
        product = cartItem.product
        ProductPrice = cartItem.price 


        updatedQuantity = int(request.data['quantity'])
        oldquantity =  cartItem.quantity

        oldPrice = oldquantity * ProductPrice
        updatedPrice = updatedQuantity * ProductPrice

        data = {'cart': cart.id, 'product': product.id,'quantity': updatedQuantity, 'price': ProductPrice}

        serializer = CartItemSerializer(cartItem,data = data)

        if serializer.is_valid():
            cart.total_items -= oldquantity
            cart.total_amount -= oldPrice

            cart.total_items += updatedQuantity
            cart.total_amount += updatedPrice
            

            cart.save()
            serializer.save()
            return Response(serializer.data)




    def delete(self,request,pk):
        cart = Cart.objects.get(user = request.user)
        cartItem = get_object_or_404(CartItem,id = pk)
        quantity = cartItem.quantity
        price = cartItem.price

        totalCartItemPrice = quantity * price
        cart.total_amount -= totalCartItemPrice
        cart.total_items -= quantity
        cart.save()
        cartItem.delete()

        return Response({"message" : "CartItem Deleted"})
