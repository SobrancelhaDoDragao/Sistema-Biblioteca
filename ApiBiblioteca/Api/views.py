from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, LivroSerializer, EmprestimoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets,filters,status

from django.conf import settings

from PIL import Image


from .models import CustomUser as User
from .models import Livro, Emprestimo

@api_view(['GET'])
def getRoutes(request):
    """
    Todas as url da Api biblioteca
    """

    routes = [
        '------- Rotas que não precisa estar autenticado -----',
        'cadastro/',
        'VerifyAuthenticated/',
        'token/',
        'token/refresh/',
        '------- Precisa estar autenticado -----',
        'UserLogado/',
        'users/',
        'livros/'
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


class CadastroUser(APIView):
    """
    View para cadastro de usuario
    """
   
    def post(self, request, format=None):

        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserCRUD(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
   

    filter_backends = [filters.SearchFilter]
    search_fields = ['email','id']
    
    def UserLogadoData(self, request, *args, **kwargs):
   
        user = User.objects.get(id=request.user.id)
        # Para gerar a imagem com URL completa precisa passar o contexto 
        serializer = UserSerializer(user,context={'request': request})
      
        return Response(serializer.data)

class LivroCRUD(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Livro.objects.all().order_by('-data_criacao')
    serializer_class = LivroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'editora','autor','genero']


class EmprestimoCRUD(viewsets.ModelViewSet):

    queryset = Emprestimo.objects.all().order_by('data_criacao')
    serializer_class = EmprestimoSerializer

    
 