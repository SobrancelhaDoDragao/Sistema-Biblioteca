from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, LivroSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from django.http import Http404
import base64
from PIL import Image
from io import BytesIO
import datetime
import os


from .models import CustomUser as User
from .models import Livro

def salvarImagem(data_url,path,nome):
    """
    Função que salva a imagem e retorna o nome do arquivo
    """
    # Removendo informações iniciais
    data_url = data_url.split(',')[1]
    # Decodificando
    img_bytes = base64.b64decode(data_url)
            
    img = Image.open(BytesIO(img_bytes))
            
    # Usar a data para sempre ter um nome unico
    now = datetime.datetime.now()

    # Criar um nome de arquivo único com a data e hora atual
    filename = nome + now.strftime("%Y%m%d%H%M%S") + ".png"

    img.save(f'{path}{filename}')

    return filename


@api_view(['GET'])
def getRoutes(request):
    """
    Todas as url da Api biblioteca
    """

    routes = [
        'api/createuser',
        'api/user/',
        'api/token',
        'api/token/refresh',
        'api/VerifyAuthenticated',
        'api/createlivro/',
        'api/livro/'
    ]

    return Response(routes)


class VerifyAuthenticated(APIView):
    """
    Verificando se o usuario está logado
    """
 
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        
        response = {
            'Authenticated':True
        }
        #request.user
        return Response(response)


class UserList(APIView):
    """
    List all user, or create a new user.
    """
    def get(self, request, format=None):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
          
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create
        """

        serializer =  UserSerializer(data=request.data)
              
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_Detail(APIView):
    """
    Recuperar, Atualizar ou deletar o usuario
    """
    permission_classes = [IsAuthenticated]

    def get_object(self,request):

        try:
            return User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """
        Retrieve
        """
  
        user = self.get_object(request)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, format=None):
        """
        Update 
        """
        user = self.get_object(request)

        try:
            # Caso seja enviado uma foto
            data_url = request.data['foto'] 

            path = 'Api/static/img/FotoPerfil/'
            nome = 'fotodeperfil'

            filename = salvarImagem(data_url,path,nome)
                
            # Salvando o nome do arquivo no banco
            request.data['foto'] = filename
        except:
            pass


        serializer = UserSerializer(user, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """
        Delete
        """
        user = self.get_object(request)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LivroList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    """
    Exibir todos os livros ou adicionar um novo livro
    """

    queryset = Livro.objects.all().order_by('-data_criacao')
    serializer_class = LivroSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
          

    def post(self, request, format=None):
        """
        Url para cadastrar livro
        """
        
        data_url = request.data['capa'] 
        
        path = 'Api/static/img/CapasLivros/'
        nome = 'capa'

        filename = salvarImagem(data_url,path,nome)
        
        # Salvando o nome do arquivo no banco
        request.data['capa'] = filename

        serializer = LivroSerializer(data=request.data)
              
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Livro_Detail(APIView):
    """
    Recuperar, Atualizar ou deletar livro
    """
    #permission_classes = [IsAuthenticated] 

    def get_object(self,request):

        try:
            return Livro.objects.get(id=request.data['id'])
        except Livro.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        """
        Retrieve
        """
  
        livro = self.get_object(request)
       
        serializer = LivroSerializer(livro)

        return Response(serializer.data)

    def put(self, request, format=None):
        """
        Update 
        """
        livro = self.get_object(request)
         
        try:
            # Caso seja enviado uma nova capa
            data_url = request.data['capa'] 

            path = 'Api/static/img/CapasLivros/'
            nome = 'capa'

            filename = salvarImagem(data_url,path,nome)
                
            # Salvando o nome do arquivo no banco
            request.data['capa'] = filename

            os.remove(f'Api/static/img/CapasLivros/{livro.capa}')
        except:
            pass

        serializer = LivroSerializer(livro, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """
        Delete
        """
        livro = self.get_object(request)

        os.remove(f'Api/static/img/{livro.capa}')
        
        livro.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
