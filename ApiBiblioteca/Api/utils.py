"""
Arquivo para armazenar funções que serao usadas em todo sistema
"""
from PIL import Image, ImageDraw, ImageFont
from random import randint
from io import BytesIO

def ResizeCapa(image,image_size):
    """
    Função para redimensionar uma imagem

    Input: image, image_size
    Output: Image file
    """
    # Salvando a imagem no objeto BytesIO, ao em vez de salvar no HD
    # Buffer para salvar a imagem
    image_io = BytesIO()

    scaled_image = Image.open(image)
    scaled_image = scaled_image.resize(image_size)

    # Salvando a imagem no objeto BytesIO, ao em vez de salvar no HD
    scaled_image.save(image_io, format='png')

    return image_io

def CreateCapa(width,height,nome,autor):
    """
    Função parar criar uma capa de livro

    Input: width, height, nome, autor
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

    image_size = (width,height)
    # Capa tera um cor escolhida aleatoriamente
    image = Image.new('RGB', image_size, backGround[randint(0,6)])
    
    pen = ImageDraw.Draw(image)
   
    # Obter o caminho da fonte padrão da pillow
    h1 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
    h2 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", (font_size - 20))

    textos_para_escrever = [nome_do_livro,nome_do_autor]
    
    altura_pocisao = 2 + len(textos_para_escrever)

    for count, texto in enumerate(textos_para_escrever,start=1):

        fonte = h1 if count == 1 else h2
        
        # width, height do texto
        w_text, h_text = pen.textsize(texto, font=fonte)

        if w_text > width:
            quebra_de_linha = texto.split(" ",2)
            
            altura_pocisao += 1

            for i, linha in enumerate(quebra_de_linha,start=1):
                
                w_text, h_text = pen.textsize(linha, font=fonte)
                # Calculando a posição centralizado do titulo e autor
                x,y = (width - w_text) // 2, height // altura_pocisao - h_text
                pen.text((x,y),linha,font=fonte, fill=black)
                altura_pocisao -= 1
        else:
            # Calculando a posição centralizado do titulo e autor
            x,y = (width - w_text) // 2, height // altura_pocisao - h_text
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

