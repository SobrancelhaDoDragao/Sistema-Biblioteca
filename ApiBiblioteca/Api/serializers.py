from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Livro


class UserSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = CustomUser 
        fields = ('id','nome', 'email', 'foto','password','is_admin')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        if validated_data['is_admin']:
            user = CustomUser.objects.create_superuser(validated_data['nome'],validated_data['email'],validated_data['password'])
            return user
        else:
            user = CustomUser.objects.create_user(validated_data['nome'],validated_data['email'],validated_data['password'])
            return user

      
        
    
class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = ('id','nome','capa','autor','editora','genero','descricao')


