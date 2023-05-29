from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

import os
from datetime import datetime, timedelta
from .utils import CreateCapa, ResizeCapa


# Fuso horario
from django.utils.timezone import now

storageCapas = FileSystemStorage(location=f"{settings.MEDIA_ROOT}/CapasLivros",base_url=f'{settings.MEDIA_URL}CapasLivros')
storageFotos = FileSystemStorage(location=f"{settings.MEDIA_ROOT}/FotosUsuarios",base_url=f'{settings.MEDIA_URL}FotosUsuarios')

class MyUserManager(BaseUserManager):
    def create_user(self, nome, email, password=None):
        """
        Creates and saves a User 
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, password=None):
        """
        Creates and saves a superuser 
        """
        user = self.create_user(
            email=email,
            password=password,
            nome=nome,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # Campos adicionais
    nome = models.CharField(max_length=50)
    foto = models.ImageField(storage=storageFotos,null=True, blank=True)

    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class Livro(models.Model):

    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    capa = models.ImageField(storage=storageCapas,null=True, blank=True)
    editora = models.CharField(max_length=50,null=True, blank=True)
    genero = models.CharField(max_length=50,null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def save(self,*args,**kwargs):
        """
        Diminuindo o tamanho das imagens para economizar espaço e padronizar, ou criando uma capa caso não tenha
        """
        width = settings.CAPAWIDTH
        height = settings.CAPAHEIGHT

        image_size = (width,height)
        
        # Quando é enviado uma capa
        if self.capa:
            try:
                livro = Livro.objects.get(id=self.id)
                
                if livro.capa != self.capa:
                    # Redimensionando imagem 
                    scaled_image = ResizeCapa(self.capa, image_size)
                    # 'save=false' por que tem salvar apenas no final do try
                    self.capa.save(f"{self.nome}.png", scaled_image, save=False)

            except Livro.DoesNotExist:
                # Redimensionando imagem 
                scaled_image = ResizeCapa(self.capa, image_size)
                # 'save=false' por que tem salvar apenas no final do try
                self.capa.save(f"{self.nome}.png", scaled_image, save=False)
            

        # Caso não tenha uma capa então uma é criada
        else:
            
            image = CreateCapa(width,height,self.nome,self.autor)
            
            self.capa.save(f"{self.nome}.png", image, save=False)
     
        super().save(*args, **kwargs)
            

class Emprestimo(models.Model):

    EMPRESTADO = 'emprestado'
    ATRASADO = 'atrasado'
    DEVOLVIDO = 'devolvido'

    STATUS_CHOICES = [
        (EMPRESTADO, 'Emprestado'),
        (ATRASADO, 'Atrasado'),
        (DEVOLVIDO, 'Devolvido'),
    ]
     
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default=EMPRESTADO,choices=STATUS_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(default = now() + timedelta(days=30))


@receiver(pre_delete, sender=Livro)
def deleteCapa(sender,instance, **kwargs):
    # Removendo capa dos arquivos
    os.remove(f"{settings.MEDIA_ROOT}/CapasLivros/{instance.capa}")


@receiver(pre_save, sender=Livro)
def deleteCapaAntiga(sender,instance, **kwargs):

    try:
        livro = Livro.objects.get(id=instance.id)
        
        if livro.capa != instance.capa:
                # Removendo capa dos arquivos
                os.remove(f"{settings.MEDIA_ROOT}/CapasLivros/{livro.capa}")
    except Livro.DoesNotExist:
        pass


@receiver(pre_save, sender=CustomUser)
def deleteFotoAntiga(sender,instance, **kwargs):

    try:
        user = CustomUser.objects.get(id=instance.id)
        
        if user.foto != instance.foto:
                # Removendo foto dos arquivos
                os.remove(f"{settings.MEDIA_ROOT}/FotosUsuarios/{user.foto}")
    except:
        pass