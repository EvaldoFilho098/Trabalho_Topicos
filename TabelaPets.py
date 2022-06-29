from tkinter import *
from tkinter import ttk
from Tabelas import Tabelas

root = Tk()

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
    def __init__(self,master):
        self.root = master
        self.Tela()
        self.frames_da_tela()
        self.inserir_widgets()
        self.inserir_tabela()
        try:
            root.mainloop()
        except:
            self.root.mainloop()
    
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
        self.lb_Filtros.Texto.place(relx = 0.40,rely=0)
        
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
        self.lb_Buscar = Textos(self.frame_1,'Buscar')
        self.lb_Buscar.Texto.place(relx=0.33,rely=0.9,relwidth=0.15,relheight=0.15)
        self.bt_Buscar = Botoes(self.frame_1,'Buscar')
        self.bt_Buscar.Botao.config(command=self.Buscar)
        self.bt_Buscar.Botao.place(relx=0.33,rely=0.9,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.lb_Limpar = Textos(self.frame_1,'Limpar')
        self.lb_Limpar.Texto.place(relx=0.50,rely=0.9,relwidth=0.15,relheight=0.15)
        self.bt_Limpar = Botoes(self.frame_1,'Limpar')
        self.bt_Limpar.Botao.config(command=self.Limpar)
        self.bt_Limpar.Botao.place(relx=0.50,rely=0.9,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.bt_Selecionar = Botoes(self.frame_2,'Selecionar')
        self.bt_Selecionar.Botao.config(command=self.Selecionar)
        self.bt_Selecionar.Botao.place(relx=0.45,rely=0.9)
        
               
    def inserir_tabela(self):
        self.Tabela_Agrs = Tabelas(self.frame_2,
                                  colunas = ('ID','FOTO','NOME','RAÇA','IDADE'),
                                  qtd_linhas = 20,
                                  largura = 120,
                                  lar_min = 50)
        self.Tabela_Agrs.Listagem.place(relx=0,rely=0,relwidth=0.982,relheight=0.8)
        self.Tabela_Agrs.Barra_Y.place(relx=0.984 ,rely=0,relheight=0.835)
        self.Tabela_Agrs.Barra_X.place(relx=0.0 ,rely=0.799,relwidth=0.982)

        def Pegar_Infos(event):
            nodeId_1 = self.Tabela_Agrs.Listagem.focus()
            id = self.Tabela_Agrs.Listagem.item(nodeId_1)['values'][0]
            #Infos(self.root,id)
        
        self.Tabela_Agrs.Listagem.bind('<Double-1>',Pegar_Infos)
        
        self.mostrar_na_tabela()
    
    def mostrar_na_tabela(self,filtros={}): 
        self.Tabela_Agrs.Listagem.delete(*self.Tabela_Agrs.Listagem.get_children())
        #self.Lista_AGRs = BD.Select_Columns(
        #    colunas=('ID_AGR','NOME','LOCAL','TELEFONE','EMAIL','TERMO','ACMETA','SOLUTI'),
        #    tabela='AGR',
        #    filtros=filtros,
        #    )
        self.Lista = [('1','2','3','4','5')]
        self.Tabela_Agrs.Inserir(self.Lista)
    
    def Selecionar(self):
        pass
    
    def Buscar(self):
        busca = {}
        nome = self.et_Nome.Entrada.get()
        if nome != '':
            busca['NOME'] = nome.upper()
            
        cod_pet = self.et_Cod_Pet.Entrada.get()
        if cod_pet != '':
            busca['ID'] = cod_pet.upper()
            
        raca = self.et_Raca.Entrada.get()
        if raca :
            busca['RACA'] ='ATIVO'
        
        self.mostrar_na_tabela(busca)
    
    def Limpar(self):
        self.et_Nome.Entrada.delete(0,END)
        self.et_Cod_Pet.Entrada.delete(0,END)
        self.et_Raca.Entrada.delete(0,END)
        
        self.mostrar_na_tabela()
        
    
VisualizarPets(root)