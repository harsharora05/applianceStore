from django.shortcuts import render
from django.contrib.auth.models  import User
from rest_framework.views import APIView,Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from User.api.serializer import RegisterSerializer

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refreshToken = RefreshToken.for_user(user)
            return Response({
                "user" : serializer.data,
                "refreshToken" :str( refreshToken) ,
                "accessToken" : str(refreshToken.access_token)
            },status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

     

        
    