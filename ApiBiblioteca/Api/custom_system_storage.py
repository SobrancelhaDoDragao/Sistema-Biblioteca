import os
from datetime import datetime, timezone
from urllib.parse import urljoin
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from random import randint

from django.conf import settings
from django.core.files import File, locks
from django.core.files.move import file_move_safe
from django.core.signals import setting_changed
from django.utils._os import safe_join
from django.utils.deconstruct import deconstructible
from django.utils.encoding import filepath_to_uri
from django.utils.functional import cached_property

from django.core.files.storage import Storage


class CoverManagementSystem(Storage):
    """
    Standard filesystem storage
    """

    # The combination of O_CREAT and O_EXCL makes os.open() raise OSError if
    # the file already exists before it's opened.
    OS_OPEN_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)

    def __init__(self):
        
        self._location = f"{settings.MEDIA_ROOT}/CapasLivros"
        self._base_url = f'{settings.MEDIA_URL}CapasLivros'

        self._width = settings.CAPAWIDTH
        self._height = settings.CAPAHEIGHT
        
        setting_changed.connect(self._clear_cached_properties)

    def _clear_cached_properties(self, setting, **kwargs):
        """Reset setting based property values."""
        if setting == "MEDIA_ROOT":
            self.__dict__.pop("base_location", None)
            self.__dict__.pop("location", None)
        elif setting == "MEDIA_URL":
            self.__dict__.pop("base_url", None)
      
    def _value_or_setting(self, value, setting):
        return setting if value is None else value

    @cached_property
    def base_location(self):
        return self._value_or_setting(self._location, settings.MEDIA_ROOT)

    @cached_property
    def location(self):
        return os.path.abspath(self.base_location)

    @cached_property
    def base_url(self):
        if self._base_url is not None and not self._base_url.endswith("/"):
            self._base_url += "/"
        return self._value_or_setting(self._base_url, settings.MEDIA_URL)

    @cached_property
    def directory_permissions_mode(self):
        return self._value_or_setting(
            self._directory_permissions_mode, settings.FILE_UPLOAD_DIRECTORY_PERMISSIONS
        )

    def _open(self, name, mode="rb"):
        return File(open(self.path(name), mode))

    def _save(self, name, content):
          
        full_path = self.path(name)

        # Criando a pasta casa não exista
        directory = os.path.dirname(full_path)
        try:
            os.makedirs(directory, exist_ok=True)
        except FileExistsError:
            raise FileExistsError("%s exists and is not a directory." % directory)

        # There's a potential race condition between get_available_name and
        # saving the file; it's possible that two threads might return the
        # same name, at which point all sorts of fun happens. So we need to
        # try to create the file, but if it already exists we have to go back
        # to get_available_name() and try again.
        
        while True:
            try:
                # This file has a file path that we can move.
                if hasattr(content, "temporary_file_path"):
                    file_move_safe(content.temporary_file_path(), full_path)

                # This is a normal uploadedfile that we can stream.
                else:
                    # The current umask value is masked out by os.open!
                    fd = os.open(full_path, self.OS_OPEN_FLAGS, 0o666)
                    _file = None
                    try:
                        locks.lock(fd, locks.LOCK_EX)
                        for chunk in content.chunks():
                            if _file is None:
                                mode = "wb" if isinstance(chunk, bytes) else "wt"
                                _file = os.fdopen(fd, mode)
                            _file.write(chunk)
                    finally:
                        locks.unlock(fd)
                        if _file is not None:
                            _file.close()
                        else:
                            os.close(fd)
            except FileExistsError:
                # A new name is needed if the file exists.
                name = self.get_available_name(name)
                full_path = self.path(name)
            else:
                # OK, the file save worked. Break out of the loop.
                break

        # Ensure the saved path is always relative to the storage root.
        name = os.path.relpath(full_path, self.location)
        # Ensure the moved file has the same gid as the storage root.
        self._ensure_location_group_id(full_path)
        # Store filenames with forward slashes, even on Windows.
        return str(name).replace("\\", "/")
    
    def cover_resize(self,image):
        """
        Função para redimensionar uma imagem

        Input: image, image_size
        Output: Image file
        """
        image_size = (self._width,self._height)
        # Salvando a imagem no objeto BytesIO, ao em vez de salvar no HD
        # Buffer para salvar a imagem
        image_io = BytesIO()

        scaled_image = Image.open(image)
        scaled_image = scaled_image.resize(image_size)

        # Salvando a imagem no objeto BytesIO, ao em vez de salvar no HD
        scaled_image.save(image_io, format='png')

        return image_io

    def CreateCapa(self,nome,autor):
        """
        Função parar criar uma capa de livro

        Input:nome, autor
        Output: Pillow object Image
        """

        nome_do_livro = nome
        nome_do_autor = autor
        font_size = 60
        black = (0, 0, 0)
        backGround = [(255,255,100),(146, 82, 162),(146, 82, 43),(255, 124, 43),(137, 251, 70),(137, 57, 146),(88, 167, 146)]
    
        # Salvando a imagem no objeto BytesIO, ao em vez de salvar no HD
        # Buffer para salvar a imagem
        image_io = BytesIO()
    
        image_size = (self._width,self._height)
        # Capa tera um cor escolhida aleatoriamente
        image = Image.new('RGB', image_size, backGround[randint(0,6)])
        
        pen = ImageDraw.Draw(image)
    
        # Obter o caminho da fonte padrão da pillow
        h1 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
        h2 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", (font_size - 20))

        textos_para_escrever = [nome_do_livro,nome_do_autor]
        
        altura_pocisao = 2 + len(textos_para_escrever)

        for count, texto in enumerate(textos_para_escrever):

            fonte = h1 if count == 0 else h2
            
            # width, height do texto
            w_text, h_text = pen.textsize(texto, font=fonte)

            if w_text > self._width:
                quebra_de_linha = texto.split(" ",2)
                
                altura_pocisao += 1

                for linha in quebra_de_linha:
                    
                    w_text, h_text = pen.textsize(linha, font=fonte)
                    # Calculando a posição centralizado do titulo e autor
                    x,y = (self._width - w_text) / 2, (self._height - h_text) / altura_pocisao 
                    pen.text((x,y),linha,font=fonte, fill=black)
                    altura_pocisao -= 1
            else:
                # Calculando a posição centralizado do titulo e autor
                x,y = (self._width - w_text) / 2, (self._height - h_text) / altura_pocisao 
                # Escrevendo na imagem
                pen.text((x,y),texto,font=fonte, fill=black)
                altura_pocisao -= 1
        
        # Para desenhar uma linha é preciso do ponto do comeco(x,y) e o ponto no final(x,y). E a linha ligará os pontos. 
        # X = width, y = height 
        # Como a linha é reta, a altura do começo e do final são as mesmas

        # Desenhando linha
        draw = ImageDraw.Draw(image) 

        Altura_da_linha = (y + h_text) + h_text * 0.15

        StartX = x + w_text  # Pocisao no eixo X, Width ou Largura
        StartY = Altura_da_linha  # Pocisao no eixo Y, Height ou Altura
        
        EndX = x # Width ou Largura
        EndY = Altura_da_linha  # Height ou Altura 

        draw.line((StartX,StartY,EndX,EndY), fill=black,width=3)

        # Salvando imagem no buffer
        image.save(image_io,format='png')

        return image_io

    def _ensure_location_group_id(self, full_path):
        if os.name == "posix":
            file_gid = os.stat(full_path).st_gid
            location_gid = os.stat(self.location).st_gid
            if file_gid != location_gid:
                try:
                    os.chown(full_path, uid=-1, gid=location_gid)
                except PermissionError:
                    pass

    def delete(self, name):
        if not name:
            raise ValueError("The name must be given to delete().")
        name = self.path(name)
        # If the file or directory exists, delete it from the filesystem.
        try:
            if os.path.isdir(name):
                os.rmdir(name)
            else:
                os.remove(name)
        except FileNotFoundError:
            # FileNotFoundError is raised if the file or directory was removed
            # concurrently.
            pass

    def exists(self, name):
        return os.path.lexists(self.path(name))

    def listdir(self, path):
        path = self.path(path)
        directories, files = [], []
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    directories.append(entry.name)
                else:
                    files.append(entry.name)
        return directories, files

    def path(self, name):
        return safe_join(self.location, name)

    def size(self, name):
        return os.path.getsize(self.path(name))

    def url(self, name):
        if self.base_url is None:
            raise ValueError("This file is not accessible via a URL.")
        url = filepath_to_uri(name)
        if url is not None:
            url = url.lstrip("/")
        return urljoin(self.base_url, url)

    def _datetime_from_timestamp(self, ts):
        """
        If timezone support is enabled, make an aware datetime object in UTC;
        otherwise make a naive one in the local timezone.
        """
        tz = timezone.utc if settings.USE_TZ else None
        return datetime.fromtimestamp(ts, tz=tz)

    def get_accessed_time(self, name):
        return self._datetime_from_timestamp(os.path.getatime(self.path(name)))

    def get_created_time(self, name):
        return self._datetime_from_timestamp(os.path.getctime(self.path(name)))

    def get_modified_time(self, name):
        return self._datetime_from_timestamp(os.path.getmtime(self.path(name)))

    def get_storage_class(import_path=None):
        return import_string(import_path or settings.DEFAULT_FILE_STORAGE)