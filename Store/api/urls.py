from django.urls import path,include
from Store.api.views import ProductCreateListView,ProductListUpdateView,ProductSearchListView
urlpatterns = [

    path('product/create/',ProductCreateListView.as_view(),name = 'Product_Create'),
    path('product/',ProductSearchListView.as_view(),name = 'Product_Create'),
    path('product/<int:pk>/',ProductListUpdateView.as_view(),name = 'Product_List'),


]