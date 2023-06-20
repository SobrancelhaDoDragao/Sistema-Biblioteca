from rest_framework.test import APITestCase, APILiveServerTestCase
from rest_framework import status
from django.urls import reverse
from django_seed import Seed
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os

from .models import CustomUser as User
from .models import Livro
from .custom_system_storage import CoverManagementSystem

from rest_framework.test import APIClient


class TestBase(APITestCase):
    """
    Classe com metodos padrões que serão usadas em todos os testes
    """
    seeder = Seed.seeder()
    storage = CoverManagementSystem()

    # urls relacionas a usuarios
    cadastro_url = reverse('cadastro')
    user_url_data = '/user/'
    users_url_admin = '/all_users/'

    # urls relacionas a livros
    livros_url = '/livros/'

    # urls relacionadas a autenticação
    token_url = reverse('token_obtain_pair')
    VerifyAuthenticated = reverse('VerifyAuthenticated')

    # urls relacionadas a emprestimos
    # all_emprestimos_users = reverse('all_emprestimos_users')
    emprestimos_url = '/emprestimos/'

    def cadastro_user(self,admin=False):
        """
        Função que cadastra um usuario no sistema

        Input: admin, padrão False.
        Output: Dados do usuario, retorno da response
        """
        data = {'nome':self.seeder.faker.user_name(),'email':self.seeder.faker.email(),'password':'123','is_admin':admin}

        response = self.client.post(self.cadastro_url, data, format='json')

        return data, response

    def cadastro_livro(self,capa=''):
        """
        Métododo para cadastrar livro

        Input: None ou imagem
        Output: Dados do livro, retorno da response
        """
        # Dado do livro sem capa enviar uma capa
        data = {
        "nome": self.seeder.faker.user_name(),
        "autor": self.seeder.faker.user_name(),
        "capa": capa 
        }
        # Enviando dados
        response = self.client.post(self.livros_url, data, format="multipart")

        return data, response

    def cadastro_emprestimo(self):
        """
        Cadastrando emprestimo

        Input: None
        Output: Dados do emprestimo, retorno da response
        """
        # Criando user comum que será do emprestimo
        user, response_user = self.cadastro_user()
      
        livro, reponse_livro = self.cadastro_livro()

        emprestimo_data = {'livro':reponse_livro.data['id'],'usuario':response_user.data['id']}
        
        emprestimo_response = self.client.post(self.emprestimos_url, emprestimo_data, format='json')

        return emprestimo_data, emprestimo_response
        
    def login(self,credentials):
        """
        Função para fazer o login JWT. Adiciona o token na requisição.

        Input: Credentials
        """
        token = self.client.post(self.token_url,credentials,format='json')

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['access'])

class UserTests(TestBase):
    """
    Testando funcionalidades relacionadas ao usuarios
    """

    def test_create_user(self):
        """
        Criando um usuario comum
        """
        
        data, response = self.cadastro_user()
        
        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verificando os dados salvos
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['is_admin'], data['is_admin'])

    def test_create_super_user(self):
        """
        Criando um usuario administrador
        """
        data, response = self.cadastro_user(admin=True)

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificando os dados salvos
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['is_admin'], True)
        
    def test_create_user_with_an_existing_email(self):
        """
        Criando um usuario com um email que ja existe, o sistema não deve permitir
        """
        # Criando o primeiro usuario
        User.objects.create(nome=['teste'], email='teste@gmail.com',password='123',is_admin=0)
        # Criando um segundo com email repetido
        data = {'nome':'outroUsuario','email':'teste@gmail.com','password':'123','is_admin':0}
        
        response = self.client.post(self.cadastro_url, data, format='json')
      
        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_users(self):
        """
        Recuperando todos os usuarios. Permitido apenas admin.
        """
        # Criando um usuario comum para o login
        data, response = self.cadastro_user()

        # Logando como usuario comum
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)
        
        # Retornando usuarios
        response = self.client.get(self.users_url_admin)

        # Verificando a resposta, não pode permitir acesso de usuarios comuns
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Criando um usuario admin para fazer o login
        data, response = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)

        # Retornando usuarios
        response = self.client.get(self.users_url_admin)
        
        # O admin deve ter acesso
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Vericando a quantidade de usuarios retornada
        self.assertEqual(response.data['count'],2)

    def test_retrieve_one_user(self):
        """
        Recuperando um usuario especifico, um usuario como deve ter apenas o proprio dados retornado
        """
        # Criando um usuario comum
        data, response = self.cadastro_user()

        # Logando
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)
        
        response = self.client.get(f"{self.user_url_data}{response.data['id']}/")
        
        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificando os dados 
        self.assertEqual(response.data['nome'], f"{data['nome']}")
        self.assertEqual(response.data['email'], f"{data['email']}")
        self.assertEqual(response.data['is_admin'], data['is_admin'])
    
    def test_edit_user(self):
        """
        Editando um usuario. Verificando se o usuario pode editar seus proprios dados.
        """
        # Criando um usuario comum
        data, response = self.cadastro_user()

        # Logando
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)

        # Alterando o nome
        data = {'nome':'outronome','email':data['email'],'password':data['password'],'is_admin':data['is_admin']}

        response = self.client.put(f"{self.user_url_data}{response.data['id']}/", data, format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificando se foi alterado
        self.assertEqual(response.data['nome'], data['nome'])
    
    def test_delete_user(self):
        """
        Verificando se o usuario consegue deletar seus dados
        """
        # Criando um usuario 
        data, response = self.cadastro_user()

        # Logando
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)

        # Deletando usuario
        response = self.client.delete(f"{self.user_url_data}{response.data['id']}/", format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class LivroTests(TestBase):
    """
    Testando funcionalidades relacionadas ao livros
    """

    def test_acesso_views(self):
        """
        Verificando se usuarios comums tem acesso a view de admins
        """
        # Criando um usuario comum
        data, response = self.cadastro_user()

        # Logando 
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)

        # POST - Criação de livro
        data, response = self.cadastro_livro()

        # Verificando a resposta, não pode permitir acesso de usuarios comuns
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_create_livro_sem_capa(self):
        """
        Criando um livro sem enviar uma capa e verificando se capa foi criada corretamente

        Somente admin podem criar livro
        """
        # Criando um usuario admin para fazer o login
        data, response = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)
        
        # Criar um livro sem capa
        data, response = self.cadastro_livro()

        # Verificando se foi criado com sucesso
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Recuperando do banco para ter acesso ao metodo path
        livro = Livro.objects.get(id=response.data['id'])

        # Verificando se o arquivo foi salvo
        self.assertTrue(self.storage.exists(livro.capa.path))

        # Verificando se foi salvo corretemente
        self.assertEqual(livro.nome, data['nome'])
        self.assertEqual(livro.autor, data['autor'])

        # Deletando imagem criada
        livro.capa.delete(livro.capa)
        
        
    def test_create_livro_com_capa(self): 
        """
        Criando um livro e enviando uma capa e verificando se a capa foi redimensionada
        """
        
        # Criando um usuario admin para fazer o login
        data, response = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)
        
        nome = 'Forest Gump'
        autor = 'Winston'
        # Criando fora do padrao para testar o redimensionamento
   
        capa = self.storage.CreateCapa(nome=nome,autor=autor)
        # Preparando para enviar o arquivo
        capa = SimpleUploadedFile(f'{nome}.png',capa.getbuffer())
        
        data, response = self.cadastro_livro(capa)
           
        # Verificando se foi criado com sucesso
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        livro = Livro.objects.get(id=response.data['id'])
        
        # Verificando se o arquivo foi salvo
        self.assertTrue(self.storage.exists(livro.capa.path))
        
        # Verificando as dimensoes da capa
        self.assertEqual(livro.capa.width, settings.CAPAWIDTH)
        self.assertEqual(livro.capa.height, settings.CAPAHEIGHT)

        # Verificando os dados
        self.assertEqual(data['nome'], livro.nome)
        self.assertEqual(data['autor'], livro.autor)
     
        # Deletando imagem criada
        livro.capa.delete(livro.capa)
         
        
    def test_edit_livro(self):
        """
        Visualizando e editando dados do livro e verificando se a capa antiga foi excluida
        """
        # Criando um usuario admin para fazer o login
        data, response = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)

        # Criando capa para o teste
        capa = self.storage.CreateCapa(nome='Teste',autor='TesteAutor')

        capa = SimpleUploadedFile('Teste.png',capa.getbuffer())
        # Criando um livro
        livro = Livro.objects.create(nome='Teste', autor='teste',capa=capa)
        
        OutroNome = 'Outro nome'
        OutroAutor = 'Outro Autor'
        # Criando um nova capa para substituir a antiga
        OutraCapa = self.storage.CreateCapa(OutroNome,OutroAutor)

        OutraCapa = SimpleUploadedFile(f'{OutroNome}.png', OutraCapa.getbuffer())

        data = {
            "nome": OutroNome,
            "autor": OutroAutor,
            "capa": OutraCapa
        }
        # Alterando os dados do livro 
        response = self.client.put(f"{self.livros_url}{livro.id}/", data, format="multipart")
        
        # Verificando se a capa antiga foi deletada
        self.assertEqual(self.storage.exists(livro.capa.path), False)
        
        livro = Livro.objects.get(id=response.data['id'])

        # Verificando se o arquivo foi salvo
        self.assertTrue(self.storage.exists(livro.capa.path))

        # Verificando as dimensoes da capa
        self.assertEqual(livro.capa.width, settings.CAPAWIDTH)
        self.assertEqual(livro.capa.height, settings.CAPAHEIGHT)

        # Verificando se foi salvo corretemente
        self.assertEqual(livro.nome, data['nome'])
        self.assertEqual(livro.autor, data['autor'])

        # Deletando imagem criada
        livro.capa.delete(livro.capa)

    def test_delete_livro(self):
        """
        Deletando livro e verificando se a capa foi apagada
        """
        # Criando um usuario admin para fazer o login
        data, response = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)
        
        # Criando capa para o teste
        capa = self.storage.CreateCapa('Teste','TesteAutor')

        capa = SimpleUploadedFile('Teste.png',capa.getbuffer())

        # Criando um livro
        livro = Livro.objects.create(nome='Teste', autor='teste',capa=capa)
 
        response = self.client.get(f"{self.livros_url}{livro.id}/")
        
        # Verificando os dados
        self.assertEqual(response.data['nome'], livro.nome)
        self.assertEqual(response.data['autor'], livro.autor)

        # Verificando se a capa foi salva
        self.assertTrue(self.storage.exists(livro.capa.path))
        
        # Deletando usuario
        response = self.client.delete(f'{self.livros_url}{livro.id}/', format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificando se a capa foi deletada
        self.assertEqual(self.storage.exists(livro.capa.path),False)
       

class EmprestimoTests(TestBase):
    """
    Testando funcionalidades relacionadas a emprestimo
    """

    def test_create_with_normal_user(self):
        """
        Criando um usuario sem permissão de criar emprestimo. O sistema não deve permitir.
        """
        user, response_user = self.cadastro_user()

        credentials = {'email':user['email'],'password':user['password']}

        self.login(credentials)

        emprestimo_data = {'livro':1,'usuario':1}

        response = self.client.post(self.emprestimos_url, emprestimo_data, format='json')
        
        # Verificando a resposta, não pode permitir acesso de usuarios comuns
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_create_emprestimo(self):
        """
        Função para verificar se está sendo possivel criar emprestimo. só admin pode criar emprestimo.
        """
        # Criando admin
        user, response_user = self.cadastro_user(admin=True)
        # Logando como admin
        credentials = {'email':user['email'],'password':user['password']}

        self.login(credentials)

        data_emprestimo, emprestimo_response = self.cadastro_emprestimo()

        # Verificando a resposta 
        self.assertEqual(emprestimo_response.status_code, status.HTTP_201_CREATED)

        livro = Livro.objects.get(id=data_emprestimo['livro'])

        # Deletando imagem criada
        livro.capa.delete(livro.capa)


    def test_delete_emprestimo(self):
        """
        Testando delete de emprestimo, apenas admins podem deletar
        """
        # Criando admin
        user, response_user = self.cadastro_user(admin=True)
        # Logando como admin
        credentials = {'email':user['email'],'password':user['password']}

        self.login(credentials)

        data_emprestimo, emprestimo_response = self.cadastro_emprestimo()

        # Verificando a resposta 
        self.assertEqual(emprestimo_response.status_code, status.HTTP_201_CREATED)
   
        delete_reponse = self.client.delete(f"{self.emprestimos_url}{emprestimo_response.data['id']}/", format='json')
        
        # Verificando a resposta 
        self.assertEqual(delete_reponse.status_code, status.HTTP_204_NO_CONTENT)

        livro = Livro.objects.get(id=data_emprestimo['livro'])

        # Deletando imagem criada
        livro.capa.delete(livro.capa)

    def test_edit_emprestimo(self):
        """
        Verificando se é possivel editar emprestimo
        """
        # Criando admin
        user, response_user = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':user['email'],'password':user['password']}

        self.login(credentials)

        data_emprestimo, emprestimo_response = self.cadastro_emprestimo()

        # Novos dados do emprestimo
        data = {'livro':data_emprestimo['livro'],'usuario':data_emprestimo['usuario']}

        response = self.client.put(f"{self.emprestimos_url}{emprestimo_response.data['id']}/", data, format="multipart")

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        livro = Livro.objects.get(id=data_emprestimo['livro'])

        # Deletando imagem criada
        livro.capa.delete(livro.capa)
        
        
        
        





            
     
     

        

        
        

       

        
    

        

        
      
        



        
