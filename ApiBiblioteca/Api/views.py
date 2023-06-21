from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets,filters,status, generics

from .models import CustomUser as User
from .models import Livro, Emprestimo
from .pagination import PaginationToEmprestimo, PaginationToRecomedacao
from .serializers import UserSerializer, LivroSerializer, EmprestimoSerializer
from .permissions import ReadOnly


class getRoutes(APIView):
    """
    Todas as url da Api biblioteca
    """
    def get(self,request):

        routes = [
            'Opções de documentação da Api:',
            '/redoc/',
            '/swagger/'
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
    
    def get_queryset(self):
        # Retornando apenas os dados do usuario logado
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

    def Recomedacao(self,request):
        """
        Recomecao de livros. Por enquanto vai ser aleatorio.
        """
        # recupera 10 registros aleatórios do modelo
        random_livros = self.queryset.order_by('?')[:5]
        # Esse ('?') é um comando lento quanto tem muito items no banco de dados
        random_livros_json = self.serializer_class(random_livros, many=True,context={'request': request})

        return Response(random_livros_json.data)

    def NovosLivros(self,request):
        """
        Novos livros adicionados ao acervo
        """
        novos_livros = self.queryset.order_by('-data_criacao')[:5]
        
        novos_livros_json = self.serializer_class(novos_livros,many=True,context={'request': request})

        return Response(novos_livros_json.data)

class EmprestimoCRUD(viewsets.ModelViewSet):
    """
    Adicionar, Editar, excluir emprestimos permitido apenas a admins. Caso contrarios permitido apenas visualização.
    """
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Emprestimo.objects.all().order_by('data_criacao')
    serializer_class = EmprestimoSerializer
    pagination_class = PaginationToEmprestimo
    
    def ListarEmprestimosUsuario(self,request,pk):
        """
        Todos os empréstimos relacionados ao usuario
        """
        emprestimos = self.queryset.filter(usuario_id=pk)
        # O contexto é para retornar a url completa
        emprestimos_Json = self.serializer_class(emprestimos,many=True,context={'request': request})

        return Response(emprestimos_Json.data)


    
 