from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets,filters,status
from rest_framework import generics

from .models import CustomUser as User
from .models import Livro, Emprestimo
from .pagination import PaginationToEmprestimo, PaginationToRecomedacao
from .serializers import UserSerializer, LivroSerializer, EmprestimoSerializer
from .permissions import ReadOnly

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


class UsersAdmin(viewsets.ModelViewSet):
    """
    End-point que mostra todos os usuarios do sistema, acesso permitido apenas para admins
    """

    permission_classes = [IsAdminUser]
    # Todos os usuarios do sistema
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email','id']
    

class UserNormal(viewsets.ModelViewSet):
    """
    End-point para limitar o acesso do usuario para apenas seus proprio dados 
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    # Retornando apenas os dados do usuario logado
    def get_queryset(self):
        
        user = User.objects.filter(id=self.request.user.id)

        return user
    

class Livros(viewsets.ModelViewSet):
    """
    Adicionar, Editar, excluir permitido apenas a admins. Caso contrarios permitido apenas visualização.
    """
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Livro.objects.all().order_by('-data_criacao')
    serializer_class = LivroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'editora','autor','genero']

class EmprestimoCRUD(viewsets.ModelViewSet):
    """
    Para adicionar, visualizar, alterar e excluir emprestimos. Acesso restrito a admins. 
    """
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Emprestimo.objects.all().order_by('data_criacao')
    serializer_class = EmprestimoSerializer
    pagination_class = PaginationToEmprestimo


class ListarEmprestimosUsuario(generics.ListAPIView):
    """
    Todos os empréstimos relacionados ao usuario
    """

    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']

        emprestimos = Emprestimo.objects.filter(usuario_id=pk)
        
        return emprestimos


class Recomedacao(generics.ListAPIView):
    """
    Recomecao de livros. Por enquanto vai ser aleatorio
    """
    serializer_class = LivroSerializer
    pagination_class = PaginationToRecomedacao

    def get_queryset(self):
        
        # recupera 10 registros aleatórios do modelo
        random_items = Livro.objects.order_by('?')[:5]
        
        # Esse ('?') é um comando lento quanto tem muito items no banco de dados
        return random_items

class NovosLivros(generics.ListAPIView):
    """
    Novos livro do acervo
    """
    serializer_class = LivroSerializer
    pagination_class = PaginationToRecomedacao

    def get_queryset(self):
        
        # recupera 10 registros aleatórios do modelo
        queryset = Livro.objects.all().order_by('-data_criacao')[:5]
        
        return queryset

    
 