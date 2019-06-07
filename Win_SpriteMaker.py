import tkinter as tk
import tkinter.filedialog as tkf
from tkinter import *
from tkinter import messagebox

from SpriteMaker import SpriteMaker
import math as m
import os

from PIL import Image
from PIL import ImageTk

ROOT_TITLE = "Sprite Maker"

'''
Metas do programa:
Juntar e separar sprites sheets
mostrar ao usuario o formato final(Image Canvas e Window)
Rearrumar posiçoes de imagens 
transformar um sprite sheet em gif animado e ou video 
Fz resize dos mesmos
'''
#TODO
#criar interface grafica
#pegando um sprite ja feito e o separar novamente
#pegar um gif e transformar num sprite
#pegar um sprite em transformar num gif ou vid

class Window(Frame):
	"""docstring for Window"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		#ao ser instanciado instancia a def abaixo
		self.init_window()

	#cria um frame na janela
	def init_window(self):

		#muda o nome do topo da janela do programa
		self.master.title(ROOT_TITLE)

		#permite que o widget criado ocupe a janela principal inteira
		self.pack(fill= BOTH ,expand = 1)

		#instancia do menu
		menu = Menu(self.master)
		self.master.config(menu = menu)

		#objeto file
		file = Menu(menu)
		
		#adiciona o comando exit na lista de comandos file
		file.add_command(label = "Exit", command=self.client_exit)
		
		#cria o comando file no menu
		menu.add_cascade(label="File",menu =file)

		#objeto edit
		edit = Menu(menu)

		#cria o comando
		edit.add_command(label="Undo")
		#adiciona comando ao menu
		menu.add_cascade(label="Edit",menu = edit)


		#encerra o programa
	def client_exit(self):
		exit()


if __name__ == "__main__":
    Img = SpriteMaker()

    Img.salvaImagens('baratenha.png')
    Img.salvaImagens('baratenha2.png')
    Img.salvaImagens('baratenha3.png')
    Img.salvaImagens('baratenha4.png')
    Img.salvaImagens('baratenha5.png')
   	#Img.colunas('saida.png',3)
    Img.salvaGIF('barataANIM.gif',0.12,0)
    
    root =Tk()

    #tamanho da janela 
    root.geometry("400x300")
    root.minsize(400,300)
    #cria a instancia
    app = Window(root)
    root.mainloop()

    #Img.colunas('saida.png',3)
    #Img.salvaGIF('barataANIM.gif',0.12,0)