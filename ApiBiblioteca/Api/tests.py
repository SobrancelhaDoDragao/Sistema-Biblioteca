from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django_seed import Seed

from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import io
from django.core.files.uploadedfile import SimpleUploadedFile
import os

from .models import CustomUser as User
from .models import Livro


class UserTests(APITestCase):

    def generate_users(self,total_users):
        """
        Criando usuarios como valores aleatorias para testar
        """
        seeder = Seed.seeder()

        seeder.add_entity(User, total_users, {
            'nome': lambda x: seeder.faker.user_name(),
            'email': lambda x: seeder.faker.email(),
            'password': '123', 
            'is_admin':0
        })

        inserted_pks = seeder.execute()
    
    
    def test_create_user(self):
        """
        Criando um usuario comum
        """
        url = reverse('cadastro')

        data = {'nome':'teste','email':'teste@gmail.com','password':'123','is_admin':0}
        response = self.client.post(url, data, format='json')
        
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
        url = reverse('cadastro')

        data = {'nome':'Admin','email':'admin@gmail.com','password':'123','is_admin':1}
        response = self.client.post(url, data, format='json')
        
        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificando os dados salvos
        self.assertEqual(response.data['nome'], data['nome'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['is_admin'], data['is_admin'])

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
        Recuperando usarios
        """
        # Sem usuarios cadastrados
        response = self.client.get('/users/')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], [])
        self.assertEqual(response.data['count'], 0)

        quantidade_usuarios = 10
        # Cadastrar vários usuários
        self.generate_users(quantidade_usuarios)

        # Retornando usuarios
        response = self.client.get('/users/')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Vericando a quantidade retornada
        self.assertEqual(response.data['count'],quantidade_usuarios)

    def test_retrieve_one_user(self):
        """
        Recuperando um usuario especifico
        """

        usuario = User.objects.create(nome=['teste'], email='teste@gmail.com',password='123',is_admin=0)
        
        response = self.client.get(f"/users/{usuario.id}/")
        
        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificando os dados salvos
        self.assertEqual(response.data['nome'], f"{usuario.nome}")
        self.assertEqual(response.data['email'], f"{usuario.email}")
        self.assertEqual(response.data['is_admin'], usuario.is_admin)
    
    def test_edit_user(self):
        """
        Editando um usuario
        """
      
        usuario = User.objects.create(nome=['teste'], email='teste@gmail.com',password='123',is_admin=0)
        
        # Alterando o nome
        data = {'nome':'outronome','email':usuario.email,'password':usuario.password,'is_admin':usuario.is_admin}

        response = self.client.put(f'/users/{usuario.id}/', data, format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificando se foi alterado
        self.assertEqual(response.data['nome'], data['nome'])
    
    def test_delete_user(self):
        """
        Deletendo um usuario
        """
        
        usuario = User.objects.create(nome=['teste'], email='teste@gmail.com',password='123',is_admin=0)
        
        # Deletando usuario
        response = self.client.delete(f'/users/{usuario.id}/', format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LivroTests(APITestCase):

    def test_create_livro(self):
        """
        Criando um livro, com uma capa vermelha
        """
        
        # Criar um objeto de modelo com a imagem em memória
        model_data = {
            "nome": "Eudson",
            "autor": "autorTeste",
        }

        response = self.client.post("/livros/", model_data, format="multipart")
        
        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Deletando imagem criada
        #os.remove(f"{settings.MEDIA_ROOT}/CapasLivros/{model_data['capa']}")

       

        
    

        

        
      
        



        
