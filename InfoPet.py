from tkinter import *
from PIL import Image, ImageTk
from IMG import redimensionar

import awesometkinter as atk

from banco_de_dados import buscar_pet



class Botoes:
    def __init__(self,master,texto):
        self.botao = Button(master)
        self.botao.configure(
            text=texto,
            bg='#C4C4C4',
            fg='black',
            font=('Verdana', 10),
            width=7,
            activebackground='white',
            
        )

class Textos:
    def __init__(self,master,texto):
        self.texto = Label(master)
        self.texto.configure(
            text=texto,
            bg="#086788",
            fg="white",
            font=("verdana",10)
        )

class TextosInfos:
    def __init__(self,master,texto):
        self.texto = Label(master)
        self.texto.configure(
            text=texto,
            bg="white",
            fg="black",
            font=("verdana",18,'bold')
        )
        
class InfoPet:
    def __init__(self,master,id_pet):
        self.id_pet = id_pet
        self.root = master
        #self.root = Toplevel(master)
        
        self.tela()
        self.frames_tela()
        self.pegar_infos()
        self.adicionar_elementos()
        
        self.root.mainloop()
        #self.root.grab_set()
    
    def tela(self):
        self.root.title("Infos")
        self.root.geometry("1024x600")
        self.root.configure(bg="#086788")
        self.root.resizable(False, False)
        self.root.iconbitmap(default="Icones/Icone.ico")
    
    def frames_tela(self):
        self.frame_titulo = Frame(self.root,bg="#086788")
        self.frame_titulo.place(relx=0,rely=0,relheight=0.15,relwidth=1)
        
        self.frame_foto = Frame(self.root,bg="#086788")
        self.frame_foto.place(relx=0,rely=0.15,relheight=0.30,relwidth=1)
        
        self.quadro_foto = atk.Frame3d(self.frame_foto,bg='white')
        self.quadro_foto.place(relx=0.35,rely=0.0,relheight=0.9,relwidth=0.30)
        
        self.frame_infos = Frame(self.root,bg="#086788")
        self.frame_infos.place(relx=0,rely=0.45,relheight=0.50,relwidth=1)
        
        self.infos_1 = atk.Frame3d(self.frame_infos,bg='white')
        self.infos_1.place(relx=0.05,rely=0,relheight=0.9,relwidth=0.45)
        
        self.infos_2 = atk.Frame3d(self.frame_infos,bg='white')
        self.infos_2.place(relx=0.50,rely=0,relheight=0.9,relwidth=0.45)
    
    def pegar_infos(self):
        dados = buscar_pet(self.id_pet)
        self.Nome = dados[1]
        self.Raca = dados[2]
        self.Genero = dados[3]
        self.Idade = dados[4]
        if 'anos' not in str(self.Idade).lower():
            self.Idade = str(self.Idade) + ' Anos'
            
        self.Status = dados[5]
        self.dir_Foto = dados[6]
        print(dados)
    
    def adicionar_elementos(self):
        
        #self.Nome = 'Meg' #pegar do bd
        #self.dir_Foto = 'Fotos\\wesley.jpg'
        #self.dir_Foto = 'Fotos\\meg.jpg' #pegar do bd
        img = (Image.open(self.dir_Foto))
        self.Foto = ImageTk.PhotoImage(img)
        #self.Foto = redimensionar(img, 100,100)
        
        self.lbl_Nome = Textos(self.frame_titulo,self.Nome)
        self.lbl_Nome.texto.config(font=('verdana',24))
        self.lbl_Nome.texto.pack(side=TOP,anchor='center',pady=20)
        
        self.lbl_Foto = Label(self.quadro_foto,image=self.Foto)
        self.lbl_Foto.pack(side=TOP,anchor='center',pady=20)
        
        
        self.lbl_espaco = TextosInfos(self.infos_1,'')
        self.lbl_espaco.texto.pack(side=TOP,anchor='w',padx=50,pady=5)
        
        # -------------------------------- RACA ----------------------------------
        img = (Image.open('Icones\\raca.png'))
        self.Icone_Raca = redimensionar(img,30,30)
        self.lbl_Icone_Raca = Label(self.infos_1,bg='white',image=self.Icone_Raca)
        self.lbl_Icone_Raca.place(relx=0.05,rely=0.20)
        
        #self.Raca = 'Pitbull'
        self.lbl_Raca = TextosInfos(self.infos_1, self.Raca)
        self.lbl_Raca.texto.pack(side=TOP,anchor='w',pady=10,padx=70)
        
        # -------------------------------- IDADE ----------------------------------
        img = (Image.open('Icones\\idade.png'))
        self.Icone_Idade = redimensionar(img,30,30)
        self.lbl_Icone_Idade = Label(self.infos_1,bg='white',image=self.Icone_Idade)
        self.lbl_Icone_Idade.place(relx=0.05,rely=0.40)
        
        #self.Idade = '15 Anos'
        self.lbl_Idade = TextosInfos(self.infos_1, self.Idade)
        self.lbl_Idade.texto.pack(side=TOP,anchor='w',pady=10,padx=70)
        
        # -------------------------------- GENERO ----------------------------------
        img = (Image.open('Icones\\genero.png'))
        self.Icone_Genero = redimensionar(img,30,30)
        self.lbl_Icone_Genero = Label(self.infos_1,bg='white',image=self.Icone_Genero)
        self.lbl_Icone_Genero.place(relx=0.05,rely=0.60)
        
        #self.Genero = 'Fêmea'
        self.lbl_Genero = TextosInfos(self.infos_1, self.Genero)
        self.lbl_Genero.texto.pack(side=TOP,anchor='w',pady=10,padx=70)
        
        self.botao_ok = Botoes(self.root,'Ok')
        self.botao_ok.botao.pack(side=BOTTOM,anchor='center',pady=10)
    
x = Tk()
InfoPet(x,2)