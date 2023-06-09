from rest_framework.test import APITestCase, APILiveServerTestCase
from rest_framework import status
from django.urls import reverse
from django_seed import Seed
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from django.conf import settings
import os

from .utils import CreateCapa
from .models import CustomUser as User
from .models import Livro

from rest_framework.test import APIClient

class TestBase(APITestCase):
    """
    Classe com metodos padrões que serão usadas em todos os testes
    """

    def cadastro_user(self,admin=False):
        """
        Função que cadastra um usuario no sistema

        Input: admin, padrão False.
        Output: Dados do usuario, retorno da response
        """

        seeder = Seed.seeder()
        url = reverse('cadastro')
        data = {'nome':seeder.faker.user_name(),'email':seeder.faker.email(),'password':'123','is_admin':admin}

        response = self.client.post(url, data, format='json')

        return data, response

    def cadastro_livro(self,capa=''):
        """
        Métododo para cadastrar livro

        Input: None ou imagem
        Output: Dados do livro, retorno da response
        """

        seeder = Seed.seeder()
        
        
        #Dado do livro sem capa enviar uma capa
        data = {
        "nome": seeder.faker.user_name(),
        "autor": seeder.faker.user_name(),
        "capa": capa 
        }
        # Enviando dados
        response = self.client.post("/livros/", data, format="multipart")

        return data, response
        
    def login(self,credentials):
        """
        Função para fazer o login JWT. Adiciona o token na requisição.

        Input: Credentials
        """
        token_url = reverse('token_obtain_pair')
        token = self.client.post(token_url,credentials,format='json')

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
        url = reverse('cadastro')
        # Criando o primeiro usuario
        User.objects.create(nome=['teste'], email='teste@gmail.com',password='123',is_admin=0)
        # Criando um segundo com email repetido
        data = {'nome':'outroUsuario','email':'teste@gmail.com','password':'123','is_admin':0}
        
        response = self.client.post(url, data, format='json')
      
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
        response = self.client.get('/all_users/')

        # Verificando a resposta, não pode permitir acesso de usuarios comuns
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Criando um usuario admin para fazer o login
        data, response = self.cadastro_user(admin=True)

        # Logando como admin
        credentials = {'email':data['email'],'password':data['password']}
        self.login(credentials)

        # Retornando usuarios
        response = self.client.get('/all_users/')
        
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

        response = self.client.get(f"/user/{response.data['id']}/")
        
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

        response = self.client.put(f"/user/{response.data['id']}/", data, format='json')

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
        response = self.client.delete(f"/user/{response.data['id']}/", format='json')

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
        self.assertTrue(default_storage.exists(livro.capa.path))

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
        width = 5000
        height = 4000

        capa = CreateCapa(width,height,nome,autor)
        # Preparando para enviar o arquivo
        capa = SimpleUploadedFile(f'{nome}.png',capa.getbuffer())
        
        data, response = self.cadastro_livro(capa)
           
        # Verificando se foi criado com sucesso
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        livro = Livro.objects.get(id=response.data['id'])
        
        # Verificando se o arquivo foi salvo
        self.assertTrue(default_storage.exists(livro.capa.path))
        
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
        capa = CreateCapa(2000,2500,'Teste','TesteAutor')

        capa = SimpleUploadedFile('Teste.png',capa.getbuffer())
        # Criando um livro
        livro = Livro.objects.create(nome='Teste', autor='teste',capa=capa)
        
        OutroNome = 'Outro nome'
        OutroAutor = 'Outro Autor'
        # Criando um nova capa para substituir a antiga
        OutraCapa = CreateCapa(2000,2500,OutroNome,OutroAutor)

        OutraCapa = SimpleUploadedFile(f'{OutroNome}.png', OutraCapa.getbuffer())

        data = {
            "nome": OutroNome,
            "autor": OutroAutor,
            "capa": OutraCapa
        }
        # Alterando os dados do livro 
        response = self.client.put(f"/livros/{livro.id}/", data, format="multipart")
        
        # Verificando se a capa antiga foi deletada
        self.assertEqual(default_storage.exists(livro.capa.path), False)
        
        livro = Livro.objects.get(id=response.data['id'])

        # Verificando se o arquivo foi salvo
        self.assertTrue(default_storage.exists(livro.capa.path))

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
        capa = CreateCapa(2000,2500,'Teste','TesteAutor')

        capa = SimpleUploadedFile('Teste.png',capa.getbuffer())

        # Criando um livro
        livro = Livro.objects.create(nome='Teste', autor='teste',capa=capa)
 
        response = self.client.get(f"/livros/{livro.id}/")
        
        # Verificando os dados
        self.assertEqual(response.data['nome'], livro.nome)
        self.assertEqual(response.data['autor'], livro.autor)

        # Verificando se a capa foi salva
        self.assertTrue(default_storage.exists(livro.capa.path))
        
        # Deletando usuario
        response = self.client.delete(f'/livros/{livro.id}/', format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verificando se a capa foi deletada
        self.assertEqual(default_storage.exists(livro.capa.path),False)
       

class EmprestimoTests(TestBase):
    """
    Testando funcionalidades relacionadas a emprestimo
    """
    pass


            
     
     

        

        
        

       

        
    

        

        
      
        



        
