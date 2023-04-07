from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Livro


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser 
        fields = ('nome', 'email', 'foto','password','is_admin')

    

    def create(self, validated_data):
        """
        Criando um novo usuario e retorno o novo usuario criado
        """
      
        user = CustomUser.objects.create(
            nome= validated_data['nome'],
            email= validated_data['email'],
            is_admin =validated_data['is_admin']
        )

        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    def update(self, instance, validated_data):
        """
        Atualiza os dados do usuario e retorna o usuario com os dados atualizados
        """
        
        instance.nome = validated_data['nome']
        instance.email = validated_data['email']
        instance.foto = validated_data['foto']

        instance.save()

        return instance
    
class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = ('nome', 'editora', 'capa')

