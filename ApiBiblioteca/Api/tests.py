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

class UserTests(APITestCase):
    """
    Testando funcionalidades relacionadas ao usuarios
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
        

    def login(self,credentials):
        """
        Função para fazer o login JWT. Adiciona o token na requisição.

        Input: Credentials
        """
        token_url = reverse('token_obtain_pair')
        token = self.client.post(token_url,credentials,format='json')

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token.data['access'])
    
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

       
      

            
     
     

        

        
        

       

        
    

        

        
      
        



        
