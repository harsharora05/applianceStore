from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only =True)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
        password =serializers.CharField(write_only =True, required = True)



    def validate(self,attrs):
        if(attrs['password'] != attrs ['confirm_password']):
            raise serializers.ValidationError({"Message" : "Passwords don't match"})
        
        
        if (User.objects.filter(email = attrs['email']).exists()):
            raise serializers.ValidationError({"Message" : "Email already exists"})
        return attrs
        
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user