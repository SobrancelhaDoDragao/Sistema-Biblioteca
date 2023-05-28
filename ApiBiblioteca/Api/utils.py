"""
Arquivo para armazenar funções que serao usadas em todo sistema
"""
from PIL import Image, ImageDraw, ImageFont
from random import randint

def CreateCapa(width,height,nome,autor):
    """
    Função parar criar uma capa de livro

    Input: width, height, nome, autor
    Output: Image
    """

    nome_do_livro = nome
    nome_do_autor = autor
    font_size = 60
    black = (0, 0, 0)
    backGround = [(255,255,100),(146, 82, 162),(146, 82, 43),(255, 124, 43),(137, 251, 70),(137, 57, 146),(88, 167, 146)]

    image_size = (width,height)
    # Capa tera um cor escolhida aleatoriamente
    image = Image.new('RGB', image_size, backGround[randint(0,6)])

    texto = ImageDraw.Draw(image)
    draw = ImageDraw.Draw(image) # Para linha
              
    # Obter o caminho da fonte padrão da pillow
    Titulo = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
    Autor = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", (font_size - 20))

    # Pegando tamanho do texto
    Titulo_width, Titulo_height = texto.textsize(nome_do_livro, font=Titulo)
    Autor_width, Autor_height = texto.textsize(nome_do_autor, font=Autor)

    # Calculando a posição centralizado do titulo e autor
    Titulo_position = (((width - Titulo_width) // 	2, (height - Titulo_height) // 3))
    Autor_position = (((width - Autor_width) // 2, (height - Autor_height) // 2))

    # Para desenhar uma linha é preciso do ponto do comeco(x,y) e o ponto no final(x,y). E a linha ligará os pontos. 
    # X = width, y = height 
    # Como a linha é reta, a altura do começo e do final são as mesmas

    Altura_da_linha = (Titulo_position[1] + Titulo_height) + Titulo_height * 0.15 # Mais 15% apos o titulo

    StartX = Titulo_position[0] # Pocisao no eixo X, Width ou Largura
    StartY = Altura_da_linha  # Pocisao no eixo Y, Height ou Altura
    
    EndX = Titulo_position[0] + Titulo_width # Width ou Largura
    EndY = Altura_da_linha  # Height ou Altura 

    draw.line((StartX,StartY,EndX,EndY), fill=black,width=3)

    # Escrevendo na imagem
    texto.text(Titulo_position, nome_do_livro ,font=Titulo, fill=black)
    texto.text(Autor_position, nome_do_autor ,font=Autor, fill=black)

    return image