from PIL import Image
from PIL import ImageSequence
import numpy as np
import sys
import math


class SpriteMaker:

    #array q recebe suas imgs  para formar sprite (ja com seus parametros abertos)
    ImgAbertas = [] 
    width = []
    height = []
    numeroImagens = 0

    #Para separar as imagens e armazenar  aqui
    ImgsSaida = []

    #salva imagens no array
    def salvaImagens(self,imagen):
        self.ImgAbertas.append(Image.open(imagen,'r'))
        self.width.append(self.ImgAbertas[self.numeroImagens].size[0])
        self.height.append(self.ImgAbertas[self.numeroImagens].size[1])

        self.numeroImagens = self.numeroImagens + 1
    
    #implementar valor de distancia da separaçao de sprites?
    def separaImagens(LarguraSpr,AlturaSpr,offsetX,offsetY):

        LadoX = 0 
        LadoY = 0
        result = []
        #The crop rectangle, as a (left, upper, right, lower)-tuple.
        #separa cada imagens individualmente pelo tamanho
       
        #self.result_width = self.width[0] * nColunas
        #nLinhas = math.ceil (float(self.numeroImagens / nColunas))
        #self.result_height = self.height[0] *  nLinhas
        
        #result = Image.new('RGB', (self.result_width, self.result_height))


        #for x in range(0,valor calculado pela altura e largura)
           #self.ImgsSaida[x] = self.ImgAbertas[0].crop((LadoX, LadoY, LarguraSpr, AlturaSpr))
       
        return self.result.save(nomeDaImagem)

    
    #salva em gif ( Fz em mp4)
    def salvaGIF(self,nomeDaImagem,velocidade,repeticao):

        #loop = 0 loop eterno 1 uma vez e assim por diante
        return self.ImgAbertas[0].save(nomeDaImagem,save_all= True, append_images= self.ImgAbertas[1:],delay=velocidade,loop=repeticao)



    def horizontal(self,nomeDaImagem):
        #define a distancia em q a proxima imagem vai ser inserida na imagem final
        offsetX = 0
        offsetY = 0
        #preenche horizontalmente

        #PARTE DO PRESSUPOSTO Q TODAS AS IMAGENS TEM O MESMO TAMANHO
        #tamanho  da largura total da nova imagem
        print(self.numeroImagens)
        self.result_width = self.width[0] * self.numeroImagens
        self.result_height = self.height[0]
        self.result = Image.new('RGBA', (self.resultesult_width, self.result_height), (0,0,0,0))

        for x in range (0,self.numeroImagens):
            if x == 0:
                self.result.paste(im=self.ImgAbertas[x], box=(0, 0))
            else:
                offsetX = offsetX + self.width[x]
                self.result.paste(im=self.ImgAbertas[x], box=(offsetX, 0))
        
        return self.result.save(nomeDaImagem,format='png')

    def vertical(self,nomeDaImagem):
        #define a distancia em q a proxima imagem vai ser inserida na imagem final
        offsetX = 0
        offsetY = 0
        #prenche verticalmente

        #PARTE DO PRESSUPOSTO Q TODAS AS IMAGENS TEM O MESMO TAMANHO
        self.result_width = self.width[0]
        #tamanho  da altura total da nova imagem
        self.result_height = self.height[0] * self.numeroImagens

        self.result = Image.new('RGBA', (self.result_width, self.result_height) , (0,0,0,0))

        for x in range (0,self.numeroImagens):
            if x == 0:
                self.result.paste(im=self.ImgAbertas[x], box=(0, 0))
            else:
                offsetY = offsetY + self.height[x]
                self.result.paste(im=self.ImgAbertas[x], box=(0, offsetY))

        return self.result.save(nomeDaImagem,format='png')

    def linhas(self,nomeDaImagem,nColunas):
        #define a distancia em q a proxima imagem vai ser inserida na imagem final
        offsetX = 0
        offsetY = 0
        #limita o numero de linhas e aumenta indefinidamente  as colunas enquanto ouver imagens no vetor

        contImagens = 0
        auxColunas = -1

        self.result_width = self.width[0] * nColunas
        nLinhas = math.ceil (float(self.numeroImagens / nColunas))
        self.result_height = self.height[0] *  nLinhas
        
        self.result = Image.new('RGBA', (self.result_width, self.result_height),(0,0,0,0))

        while contImagens <  len(self.ImgAbertas):

            #do the shit
            #adiciona um na imagem maior
            #conta uma linha e volta pra zero e e vai pra proxima
            auxColunas = auxColunas + 1
           
            if auxColunas < nColunas:
                self.result.paste(im=self.ImgAbertas[contImagens], box=(offsetX, offsetY))
                offsetX = offsetX + self.width[contImagens]

            else:
                
                offsetX = 0
                offsetY = offsetY + self.height[contImagens]
                self.result.paste(im=self.ImgAbertas[contImagens], box=(offsetX, offsetY))

                offsetX = offsetX + self.width[contImagens]
                auxColunas = 0
                

            
            contImagens = contImagens + 1

        return self.result.save(nomeDaImagem,format='png')


    def colunas(self,nomeDaImagem,nLinhas):
        #define a distancia em q a proxima imagem vai ser inserida na imagem final
        offsetX = 0
        offsetY = 0
        #limita o numero de linhas e aumenta indefinidamente  as colunas enquanto ouver imagens no vetor

        contImagens = 0
        auxLinhas = -1

        self.result_height = self.height[0] *  nLinhas
        nColunas = math.ceil(float(self.numeroImagens / nLinhas))
        self.result_width = self.width[0] * nColunas
        
        self.result = Image.new('RGBA', (self.result_width, self.result_height),(0,0,0,0))

        while contImagens < len(self.ImgAbertas):

            #do the shit
            #adiciona um na imagem maior
            #conta uma linha e volta pra zero e e vai pra proxima
            auxLinhas = auxLinhas + 1
            if auxLinhas < nLinhas:
                self.result.paste(im=self.ImgAbertas[contImagens], box=(offsetX, offsetY),mask = self.ImgAbertas[contImagens])
                offsetY = offsetY + self.height[contImagens]

            else:
                
                offsetY = 0
                offsetX = offsetX + self.width[contImagens]
                self.result.paste(im=self.ImgAbertas[contImagens], box=(offsetX, offsetY),mask = self.ImgAbertas[contImagens])
                offsetY = offsetY + self.height[contImagens]
                auxLinhas = 0
                

            
            contImagens = contImagens + 1

        return self.result.save(nomeDaImagem,format='png')



    #Img.somaImagens('vertical',0,'saida.png')
'''
def merge_images(file1, file2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result.save('out.png')

'''    

#merge_images('baratenha.png','baratenha2.png')