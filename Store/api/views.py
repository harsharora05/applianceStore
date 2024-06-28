from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from rest_framework.permissions import 

from Store.api.serializer import ProductSerializer
from Store.models import Product
from Store.api.permissions import IsAdminOrReadOnly

# Create your views here.


class ProductCreateListView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes =[IsAdminOrReadOnly]



class ProductSearchListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes =[IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['category', 'company','color']
    search_fields = ['category', 'company','name']



class ProductListUpdateView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request,pk):
        data = Product.objects.get(pk = pk)
        serializer = ProductSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        oldData = Product.objects.get(pk = pk)
        serializer = ProductSerializer(oldData, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        oldData = Product.objects.get(pk = pk)
        oldData.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

