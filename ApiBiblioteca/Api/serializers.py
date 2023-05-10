from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Livro, Emprestimo


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

class EmprestimoSerializer(serializers.ModelSerializer):
    
    UsuarioDados = UserSerializer(source='usuario',read_only=True)
    LivroDados = LivroSerializer(source='livro',read_only=True)
    
    # Eu posso editar esse campo no seralizar porque ele nunca vai ser alterado, mas o devolucao não posso
    data_criacao = serializers.SerializerMethodField()


    class Meta:
        model = Emprestimo
        fields = ('id','livro','usuario','status','data_criacao','data_devolucao','UsuarioDados','LivroDados')
    

    def get_data_criacao(self, obj):
        data = obj.data_criacao
        data_formatada = data.strftime('%d/%m/%Y')
        return data_formatada

 
