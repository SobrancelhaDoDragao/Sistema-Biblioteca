from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .serializers import UserSerializer, LivroSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from rest_framework import viewsets

from django.conf import settings

from PIL import Image


from .models import CustomUser as User
from .models import Livro

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


class UserCRUD(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def UserLogadoData(self, request, *args, **kwargs):
   
        user = User.objects.get(id=request.user.id)
        # Para gerar a imagem com URL completa precisa passar o contexto 
        serializer = UserSerializer(user,context={'request': request})
      
        return Response(serializer.data)

class LivroCRUD(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Livro.objects.all().order_by('-data_criacao')
    serializer_class = LivroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'editora','autor','genero']
    
 