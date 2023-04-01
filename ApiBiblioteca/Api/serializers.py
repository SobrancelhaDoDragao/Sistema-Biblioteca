from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser 


class UserSerializer(serializers.ModelSerializer):
    """
    Create and update user
    """
  
    class Meta:
        model = CustomUser 
        fields = ('nome', 'email', 'password')
    
    def create(self, validated_data):
        """
        Criando um novo usuario e retorno o novo usuario criado
        """
        user = CustomUser.objects.create(
            nome= validated_data['nome'],
            email= validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    def update(self, instance, validated_data):
        """
        Atualiza os dados do usurio e retorno o usuario com os dados atualizados
        """
        instance.nome = validated_data['nome']
        instance.email = validated_data['email']

        instance.save()

        return instance
    


