from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser 


class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    
    nome = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    foto = serializers.CharField(max_length=50)

    class Meta:
        model = CustomUser 
        fields = ('nome', 'email', 'foto' ,'password')
    
    def create(self, validated_data):

        user = CustomUser.objects.create(
            nome=validated_data['nome'],
            email=validated_data['email'],
            foto=validated_data['foto'],
        )

        user.set_password(validated_data['password'])
        user.save()
        
        return user
