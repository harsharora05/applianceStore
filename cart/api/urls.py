from django.urls import path
from cart.api.views import CartView,AddToCartView,UpdateCartView
urlpatterns = [
    path('cart/show/',CartView.as_view(),name = 'cart'),
    path('cart/add/<int:pk>',AddToCartView.as_view(),name = 'add-product'),
    path('cart/update/<int:pk>',UpdateCartView.as_view(),name = 'update-product'),

]