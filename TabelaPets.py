from tkinter import *
from tkinter import ttk
from IMG import redimensionar
from InfoPet import InfoPet
from Tabelas import Tabelas
import banco_de_dados as BD
from PIL import Image, ImageTk

#root = Tk()

class Entradas:
    def __init__(self, container):
        self.Entrada = Entry(container)
        self.Entrada.configure(
            bg='#C4C4C4',
            fg='black',
            width=18,
            font=('Verdana', 10)
        )

# -----------------------Class Label----------------------- #
class Textos:
    def __init__(self, container,texto,bg='#086788',fg='white'):
        self.Texto = Label(container)
        self.Texto.configure(
            text = texto,
            bg=bg,
            fg=fg,
            font=('Verdana', 10, 'bold')
        )
        
class Botoes:
    def __init__(self,container,texto):
        self.Botao = Button(container)
        self.Botao.configure(
            text=texto,
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold')
        )
        
class VisualizarPets():
    def __init__(self,master,botao='ok',tipos_pets='todos'):
        #self.root = master
        self.root = Toplevel(master)
        self.botao_final = botao
        self.tipos_pets = tipos_pets
        self.Tela()
        self.frames_da_tela()
        self.inserir_widgets()
        self.inserir_tabela()
        self.root.grab_set()
        #self.root.mainloop()
    
    def Tela(self):
         
        self.root.title("Pets")
        self.root.geometry("700x700")
        self.root.resizable(False,False)
        self.root.configure(background = "#086788")
        self.root.attributes("-alpha",0.999)
        
    def frames_da_tela(self):
        
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(
            bd = 4,
            bg = '#086788',
        )
        self.frame_1.place(relx = 0.02, rely=0.02,relwidth=0.96,relheight=0.25)
        
        self.frame_lbs = Frame(self.frame_1)
        self.frame_lbs.configure(
            bd = 4,
            bg = '#086788',
        )
        self.frame_lbs.place(relx = 0.1, rely=0.17,relwidth=0.35,relheight=0.8)
        
        self.frame_ent = Frame(self.frame_1)
        self.frame_ent.configure(
            bd = 4,
            bg = '#086788',
        )
        self.frame_ent.place(relx = 0.45, rely=0.17,relwidth=0.50,relheight=0.8)
        
        # FRAME TABELA ---------------------
        
        self.frame_2 = Frame(self.root)
        self.frame_2.configure(
            bd = 4,
            bg = '#086788',
        )
        self.frame_2.place(relx = 0.02, rely=0.29,relwidth=0.96,relheight=0.69)
    
    def inserir_widgets(self):
        
        #LABEL FRILTROS
        self.lb_Filtros = Textos(self.frame_1,'Tabela de Pets','#086788','white')
        self.lb_Filtros.Texto.config(font=('verdana',14,'bold'))
        self.lb_Filtros.Texto.place(relx = 0.38,rely=0)
        
        img = (Image.open('Icones\\atualizar.png'))
        self.Img_Atualizar= redimensionar(img,20,20)
        self.botao_atualizar = Button(self.frame_1,image=self.Img_Atualizar)
        self.botao_atualizar.config(command=self.mostrar_na_tabela,bg='#C4C4C4')
        self.botao_atualizar.place(relx=0.96,rely=0.9,relheight=0.1,relwidth=0.04)
        
        #LABELS
        self.lb_Nome = Textos(self.frame_lbs,'Nome:')
        self.lb_Nome.Texto.pack(side=TOP,anchor='e', pady=4)
        
        self.lb_Cod_Pet = Textos(self.frame_lbs,'Código Pet:')
        self.lb_Cod_Pet.Texto.pack(side=TOP,anchor='e', pady=4)
        
        self.lb_Raca = Textos(self.frame_lbs,'Raça:')
        self.lb_Raca.Texto.pack(side=TOP,anchor='e', pady=4)
        
        
        #ENTRADAS
        self.et_Nome = Entradas(self.frame_ent)
        self.et_Nome.Entrada.pack(side=TOP,anchor='w',pady=5)
        
        self.et_Cod_Pet = Entradas(self.frame_ent)
        self.et_Cod_Pet.Entrada.pack(side=TOP,anchor='w',pady=5)
        
        self.et_Raca = Entradas(self.frame_ent)
        self.et_Raca.Entrada.pack(side=TOP,anchor='w',pady=5)
        
        
        #BOTAO DE PESQUISAR
        self.bt_Buscar = Botoes(self.frame_1,'Buscar')
        self.bt_Buscar.Botao.config(command=self.Buscar)
        self.bt_Buscar.Botao.place(relx=0.33,rely=0.88,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.bt_Limpar = Botoes(self.frame_1,'Limpar')
        self.bt_Limpar.Botao.config(command=self.Limpar)
        self.bt_Limpar.Botao.place(relx=0.50,rely=0.88,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE SELECIONAR OU OK
        self.bt_Selecionar = Botoes(self.frame_2,'')
        
        if self.botao_final == 'selecionar':
            self.bt_Selecionar.Botao.config(text='Selecionar')
        else:
            self.bt_Selecionar.Botao.config(text='OK',command=self.root.destroy)
            
        self.bt_Selecionar.Botao.place(relx=0.45,rely=0.9,relwidth=0.1)
        
               
    def inserir_tabela(self):
        self.Tabela_Pets = Tabelas(self.frame_2,
                                  colunas = ('ID','NOME','RAÇA','GENERO','IDADE','STATUS'),
                                  qtd_linhas = 20,
                                  largura = 120,
                                  lar_min = 50)
        self.Tabela_Pets.Listagem.place(relx=0,rely=0,relwidth=0.982,relheight=0.8)
        self.Tabela_Pets.Barra_Y.place(relx=0.984 ,rely=0,relheight=0.835)
        self.Tabela_Pets.Barra_X.place(relx=0.0 ,rely=0.799,relwidth=0.982)

        def Pegar_Infos(event):
            nodeId_1 = self.Tabela_Pets.Listagem.focus()
            id = self.Tabela_Pets.Listagem.item(nodeId_1)['values'][0]
            InfoPet(self.root,id)
            #Infos(self.root,id)
        
        self.Tabela_Pets.Listagem.bind('<Double-1>',Pegar_Infos)
        
        self.mostrar_na_tabela()
    
    def mostrar_na_tabela(self,filtros={}): 
        self.Tabela_Pets.Listagem.delete(*self.Tabela_Pets.Listagem.get_children())
        self.Lista = BD.mostrar_pets(filtros,self.tipos_pets)
        self.Tabela_Pets.Inserir(self.Lista)
    
    def Selecionar(self):
        nodeId_1 = self.Tabela_Pets.Listagem.focus()
        self.ID_Selecionado = self.Tabela_Pets.Listagem.item(nodeId_1)['values'][0]
        self.root.destroy()
        #return id
    
    def Buscar(self):
        busca = {}
        nome = self.et_Nome.Entrada.get()
        if nome != '':
            busca['NOME_pet'] = nome.upper()
            
        cod_pet = self.et_Cod_Pet.Entrada.get()
        if cod_pet != '':
            busca['COD_pet'] = cod_pet.upper()
            
        raca = self.et_Raca.Entrada.get()
        if raca :
            busca['RACA_pet'] = raca.upper()
        
        self.mostrar_na_tabela(busca)
    
    def Limpar(self):
        self.et_Nome.Entrada.delete(0,END)
        self.et_Cod_Pet.Entrada.delete(0,END)
        self.et_Raca.Entrada.delete(0,END)
        
        self.mostrar_na_tabela()
        
#root = Tk()
#VisualizarPets(root,'ok','todos')