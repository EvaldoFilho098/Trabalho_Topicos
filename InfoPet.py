from tkinter import *
from PIL import Image, ImageTk
from CadConsulta import CadConsulta
from IMG import redimensionar
from Tabelas import Tabelas
import banco_de_dados as BD



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
        #self.root = master
        self.root = Toplevel(master)
        
        self.tela()
        self.frames_tela()
        self.pegar_infos()
        self.adicionar_elementos_frame_info1()
        self.adicionar_elementos_frame_info2()
        
        #self.root.mainloop()
        self.root.grab_set()
    
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
        
        self.quadro_foto =Frame(self.frame_foto)
        self.quadro_foto.config(
            bg = 'white',
            bd = 4,
        )
        self.quadro_foto.place(relx=0.35,rely=0.0,relheight=0.9,relwidth=0.30)
        
        self.frame_infos = Frame(self.root,bg="#086788")
        self.frame_infos.place(relx=0,rely=0.45,relheight=0.50,relwidth=1)
        
        self.infos_1 =Frame(self.frame_infos)
        self.infos_1.config(
            bg = 'white',
            bd = 4,
        )
        self.infos_1.place(relx=0.05,rely=0,relheight=0.9,relwidth=0.35)
        
        self.infos_2 =Frame(self.frame_infos)
        self.infos_2.config(
            bg = 'white',
            bd = 4,
        )
        self.infos_2.place(relx=0.415,rely=0,relheight=0.9,relwidth=0.55)
    
    def pegar_infos(self):
        dados = BD.buscar_pet(self.id_pet)
        self.Nome = dados[1]
        self.Raca = dados[2]
        self.Genero = dados[3]
        self.Idade = dados[4]
        if 'anos' not in str(self.Idade).lower():
            self.Idade = str(self.Idade) + ' Anos'
        
        self.Status = dados[5]
            
        self.dir_Foto = dados[6]
        #print(dados)
    
    def adicionar_elementos_frame_info1(self):
        
        img = (Image.open(self.dir_Foto))
        self.Foto = ImageTk.PhotoImage(img)
        #self.Foto = redimensionar(img, 100,100)
        
        self.lbl_Nome = Textos(self.frame_titulo,self.Nome)
        self.lbl_Nome.texto.config(font=('verdana',24))
        self.lbl_Nome.texto.pack(side=TOP,anchor='center',pady=20)
        
        self.lbl_Foto = Label(self.quadro_foto,image=self.Foto)
        self.lbl_Foto.pack(side=TOP,anchor='center',pady=20)
        
        self.lbl_espaco = Label(self.infos_1,text='',font=('verdana',13),bg='white')
        self.lbl_espaco.pack(side=TOP,anchor='w',padx=40)
        
        # -------------------------------- RACA ----------------------------------
        img = (Image.open('Icones\\raca.png'))
        self.Icone_Raca = redimensionar(img,28,28)
        self.lbl_Icone_Raca = Label(self.infos_1,bg='white',image=self.Icone_Raca)
        self.lbl_Icone_Raca.place(relx=0.05,rely=0.14)
        
        #self.Raca = 'Pitbull'
        self.lbl_Raca = TextosInfos(self.infos_1, self.Raca)
        self.lbl_Raca.texto.pack(side=TOP,anchor='w',pady=10,padx=60)
        
        # -------------------------------- IDADE ----------------------------------
        img = (Image.open('Icones\\idade.png'))
        self.Icone_Idade = redimensionar(img,28,28)
        self.lbl_Icone_Idade = Label(self.infos_1,bg='white',image=self.Icone_Idade)
        self.lbl_Icone_Idade.place(relx=0.05,rely=0.35)
        
        #self.Idade = '15 Anos'
        self.lbl_Idade = TextosInfos(self.infos_1, self.Idade)
        self.lbl_Idade.texto.pack(side=TOP,anchor='w',pady=10,padx=60)
        
        # -------------------------------- GENERO ----------------------------------
        img = (Image.open('Icones\\genero.png'))
        self.Icone_Genero = redimensionar(img,28,28)
        self.lbl_Icone_Genero = Label(self.infos_1,bg='white',image=self.Icone_Genero)
        self.lbl_Icone_Genero.place(relx=0.05,rely=0.55)
        
        #self.Genero = 'Fêmea'
        self.lbl_Genero = TextosInfos(self.infos_1, self.Genero)
        self.lbl_Genero.texto.pack(side=TOP,anchor='w',pady=10,padx=60)

        # -------------------------------- STAUS ----------------------------------
        img = (Image.open('Icones\\status1.png'))
        self.Icone_Status = redimensionar(img,28,28)
        self.lbl_Icone_Status = Label(self.infos_1,bg='white',image=self.Icone_Status)
        self.lbl_Icone_Status.place(relx=0.05,rely=0.77)
        
        self.lbl_Status = TextosInfos(self.infos_1, self.Status)
        self.lbl_Status.texto.pack(side=TOP,anchor='w',pady=10,padx=60)

        self.botao_ok = Botoes(self.root,'Ok')
        self.botao_ok.botao.config(command=self.root.destroy)
        self.botao_ok.botao.pack(side=BOTTOM,anchor='center',pady=10)
    
    def adicionar_elementos_frame_info2(self):

        # -------------------------------- RACA ----------------------------------
        img = (Image.open('Icones\\veterinario2.png'))
        self.Vet = redimensionar(img,28,28)
        self.lbl_Vet = Label(self.infos_2,bg='white',image=self.Vet,)
        self.lbl_Vet.place(relx=0.0,rely=0.0)
        
        self.lbl_Vet = Label(self.infos_2, text='Histórico de Consultas', bg='white',font=('verdana',14,'bold'))
        self.lbl_Vet.place(relx=0.055,rely=0.0)

        self.inserir_tabela()
        
        img = (Image.open('Icones\\atualizar.png'))
        self.Img_Atualizar= redimensionar(img,20,20)
        self.botao_atualizar = Button(self.infos_2,image=self.Img_Atualizar)
        self.botao_atualizar.config(command=self.atualizar_tabela,bg='#C4C4C4')
        self.botao_atualizar.place(relx=0.9,rely=0.0,relheight=0.1,relwidth=0.05)

        self.botao_add = Botoes(self.infos_2,'+')
        self.botao_add.botao.config(command=self.nova_consulta)
        self.botao_add.botao.place(relx=0.95,rely=0.0,relheight=0.1,relwidth=0.05)

    def atualizar_tabela(self):
        self.mostrar_na_tabela()

    def nova_consulta(self):
        CadConsulta(self.root,self.id_pet)

    def inserir_tabela(self):
        self.Tabela_Vets = Tabelas(self.infos_2,
                                  colunas = ('ID','CLINICA','HISTORICO','VALOR'),
                                  qtd_linhas = 5,
                                  largura = 50,
                                  lar_min = 50)
        self.Tabela_Vets.Listagem.place(relx=0.0,rely=0.16,relwidth=0.982,relheight=0.8)
        self.Tabela_Vets.Barra_Y.place(relx=0.984 ,rely=0.16,relheight=0.8)
        self.Tabela_Vets.Barra_X.place(relx=0.0 ,rely=0.95,relwidth=0.982)

        def Pegar_Infos(event):
            nodeId_1 = self.Tabela_Vets.Listagem.focus()
            id = self.Tabela_Vets.Listagem.item(nodeId_1)['values'][0]
            #print(id)
            #Infos(self.root,id)
        
        self.Tabela_Vets.Listagem.bind('<Double-1>',Pegar_Infos)
        
        self.mostrar_na_tabela()
    
    def mostrar_na_tabela(self,filtros={}): 
        self.Tabela_Vets.Listagem.delete(*self.Tabela_Vets.Listagem.get_children())
        self.Lista = BD.buscar_historico_pet(self.id_pet)
        self.Tabela_Vets.Inserir(self.Lista)

    
#x = Tk()
#InfoPet(x,2)