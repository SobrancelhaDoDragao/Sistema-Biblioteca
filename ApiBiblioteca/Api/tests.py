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


class UserTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create(nome=['teste'], email='teste@gmail.com',password='123',is_admin=0)

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
        
        # Salvando como atributo
        self.user = response.data

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

        print(response.data)

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
        
        usuario = User.objects.create(nome='teste', email='teste@gmail.com',password='123',is_admin=0)
        
        # Deletando usuario
        response = self.client.delete(f'/users/{usuario.id}/', format='json')

        # Verificando a resposta 
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LivroTests(APITestCase):

    def test_create_livro_sem_capa(self):
        """
        Criando um livro sem enviar uma capa e verificando se capa foi criada corretamente
        """
        
        # Criar um livro sem capa
        model_data = {
            "nome": "O Alienista",
            "autor": "Machado de assis",
            "capa": '' 
        }

        response = self.client.post("/livros/", model_data, format="multipart")

        # Verificando se foi criado com sucesso
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Recuperando do banco para ter acesso ao metodo path
        livro = Livro.objects.get(id=response.data['id'])

        # Verificando se o arquivo foi salvo
        self.assertTrue(default_storage.exists(livro.capa.path))

        # Verificando se foi salvo corretemente
        self.assertEqual(livro.nome, model_data['nome'])
        self.assertEqual(livro.autor, model_data['autor'])

        # Deletando imagem criada
        livro.capa.delete(livro.capa)
        
        
    def test_create_livro_com_capa(self): 
        """
        Criando um livro e enviando uma capa e verificando se a capa foi redimensionada
        """
        
        nome = 'Forest Gump'
        autor = 'Winston'
        # Criando fora do padrao para testar o redimensionamento
        width = 5000
        height = 4000

        capa = CreateCapa(width,height,nome,autor)
        # Preparando para enviar o arquivo
        capa = SimpleUploadedFile(f'{nome}.png',capa.getbuffer())

        model_data = {
            "nome": nome,
            "autor": autor,
            "capa": capa
        }

        response = self.client.post("/livros/", model_data, format="multipart")
        
        # Verificando se foi criado com sucesso
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        livro = Livro.objects.get(id=response.data['id'])
        
        # Verificando se o arquivo foi salvo
        self.assertTrue(default_storage.exists(livro.capa.path))
        
        # Verificando as dimensoes da capa
        self.assertEqual(livro.capa.width, settings.CAPAWIDTH)
        self.assertEqual(livro.capa.height, settings.CAPAHEIGHT)

        # Verificando os dados
        self.assertEqual(model_data['nome'], livro.nome)
        self.assertEqual(model_data['autor'], livro.autor)
     
        # Deletando imagem criada
        livro.capa.delete(livro.capa)
         
        
    def test_edit_livro(self):
        """
        Visualizando e editando dados do livro e verificando se a capa antiga foi excluida
        """
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

        # Criando capa para o teste
        capa = CreateCapa(2000,2500,'Teste','TesteAutor')

        capa = SimpleUploadedFile('Teste.png',capa.getbuffer())
        # Criando um livro
        livro = Livro.objects.create(nome='Teste', autor='teste',capa=capa)

        # Alterando os dados do livro 
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
       
      

            
     
     

        

        
        

       

        
    

        

        
      
        



        
