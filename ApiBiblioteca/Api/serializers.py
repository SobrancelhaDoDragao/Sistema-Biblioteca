from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Livro


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser 
        fields = ('id','nome', 'email', 'foto','password','is_admin')

    
class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livro
        fields = ('id','nome','capa','autor','editora','genero','descricao')


