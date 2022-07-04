from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from Tabelas import Tabelas
import banco_de_dados as BD
from IMG import redimensionar
#from index import *

# -----------------------Class Entry----------------------- #
class Entradas:
    def __init__(self, container):
        self.Entrada = Entry(container)
        self.Entrada.configure(
            bg='#C4C4C4',
            fg='black',
            width=15,
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

class Gerenciamento:
    def __init__(self,master):
        #self.root = TopLevel(master)
        self.root = master
        self.tela()
        self.inserir_frames()
        self.inserir_abas()
        #self.inserir_elementos()
        self.root.mainloop()
        #self.root.grab_set()

    def tela(self):
        self.root.title("Gerenciamento")
        self.root.geometry("1024x700")
        self.root.configure(bg="#086788")
        self.root.resizable(True, True)
        self.root.iconbitmap(default="Icones/Icone.ico")
    
    def inserir_frames(self):
        self.Frame_Titulo = Frame(self.root)
        self.Frame_Titulo.config(
            bg='#086788'
        )
        self.Frame_Titulo.place(relx=0.0,rely=0.0,relheight=0.15,relwidth=1)
        
        self.Titulo = Label(self.Frame_Titulo)
        self.Titulo.config(
            text= 'GERENCIAMENTO',
            bg = '#086788',
            fg = 'white',
            font=('verdana',24,'bold')
        )
        self.Titulo.pack(side=TOP,anchor='center',pady=25)
        
        self.Frame_Notebook = Frame(self.root)
        self.Frame_Notebook.config(
            bg='#086788'
        )
        self.Frame_Notebook.place(relx=0.0,rely=0.16,relheight=0.84,relwidth=1)
        
        
    def inserir_abas(self):
        
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", 
                        fieldbackground= '#086788',
                        foreground= '#086788',
                        background = '#086788',
                        #relief="flat",
                        )
        
        self.Notebook = ttk.Notebook(self.Frame_Notebook)
        self.Notebook.place(relx=0.02,rely=0.0,relheight=0.95,relwidth=0.95)
        #self.Notebook.pack(side=TOP, fill='both', expand=True)

        # create frames
        self.aba1 = Frame(self.Notebook, width=1000, height=460)
        self.aba2 = Frame(self.Notebook, width=1000, height=460)
        self.aba3 = Frame(self.Notebook, width=1000, height=460)

        self.aba1.pack(fill='both', expand=True)
        self.aba2.pack(fill='both', expand=True)
        self.aba3.pack(fill='both', expand=True)

        # add frames to self.Notebook
        self.Notebook.add(self.aba1, text='Verificar Adoções')
        self.Notebook.add(self.aba2, text='Verificar Adotantes/Voluntários')
        self.Notebook.add(self.aba3, text='Verificar Lares Temporários')
        
        self.aba_verif_adocao()
        self.aba_verif_adotantes()
        self.aba_verif_lares()
    
    # -------------------- ABA 1 - VERIFICAR ADOCOES ------------------
    def aba_verif_adocao(self):
        
        # ---------------------------- FILTROS ---------------------------
        self.Frame_Filtros_va = Frame(self.aba1)
        self.Frame_Filtros_va.config(
            bg = '#086788'
        )
        self.Frame_Filtros_va.place(relx=0,rely=0,relwidth=1,relheight=0.30)
        
        self.lb_Filtros_va = Textos(self.Frame_Filtros_va,'Filtros','#086788','white')
        self.lb_Filtros_va.Texto.config(font=('verdana',14,'bold'))
        self.lb_Filtros_va.Texto.place(relx = 0.48,rely=0)
        
        #LABELS
        self.lb_Nome_pess = Textos(self.Frame_Filtros_va,'Nome Adotante:')
        self.lb_Nome_pess.Texto.place(relx=0.05,rely=0.30)
        
        self.lb_cod_pess = Textos(self.Frame_Filtros_va,'Código Adotante:')
        self.lb_cod_pess.Texto.place(relx=0.05,rely=0.5)
        
        self.lb_Nome_pet = Textos(self.Frame_Filtros_va,'Nome Pet:')
        self.lb_Nome_pet.Texto.place(relx=0.40,rely=0.30)
        
        self.lb_cod_pet = Textos(self.Frame_Filtros_va,'Código Pet:')
        self.lb_cod_pet.Texto.place(relx=0.40,rely=0.5)
        
        self.lb_situacao = Textos(self.Frame_Filtros_va,'Situação:')
        self.lb_situacao.Texto.place(relx=0.67,rely=0.30)
        
        #ENTRADAS
        self.et_Nome_pess = Entradas(self.Frame_Filtros_va)
        self.et_Nome_pess.Entrada.place(relx=0.185,rely=0.30)
        
        self.et_cod_pess = Entradas(self.Frame_Filtros_va)
        self.et_cod_pess.Entrada.place(relx=0.185,rely=0.5)
        
        self.et_Nome_pet = Entradas(self.Frame_Filtros_va)
        self.et_Nome_pet.Entrada.place(relx=0.495,rely=0.30)
        
        self.et_cod_pet = Entradas(self.Frame_Filtros_va)
        self.et_cod_pet.Entrada.place(relx=0.495,rely=0.5)
        
        
        self.situacao_selecionada = StringVar()
        self.et_situacao = ttk.Combobox(self.Frame_Filtros_va, textvariable=self.situacao_selecionada)            
        self.atualiza_situacoes()
        self.et_situacao['state'] = 'readonly'
        self.et_situacao.place(relx=0.75,rely=0.30)
        
        #BOTAO DE PESQUISAR
        self.bt_Buscar = Botoes(self.Frame_Filtros_va,'Buscar')
        self.bt_Buscar.Botao.config(command=self.Buscar_Adocao)
        self.bt_Buscar.Botao.place(relx=0.35,rely=0.85,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.bt_Limpar = Botoes(self.Frame_Filtros_va,'Limpar')
        self.bt_Limpar.Botao.config(command=self.Limpar_Adocao)
        self.bt_Limpar.Botao.place(relx=0.55,rely=0.85,relwidth=0.15,relheight=0.15)

        
        # -------------------- TABELA --------------------------
        self.Frame_Tabela_va = Frame(self.aba1)
        self.Frame_Tabela_va.config(
            bg = '#086788'
        )
        self.Frame_Tabela_va.place(relx=0,rely=0.30,relwidth=1,relheight=0.60)
        
        
        self.Tabela_Adocoes = Tabelas(self.Frame_Tabela_va,
                                  colunas = ('ID','NOME ADOTANTE','NOME PET','DATA DE VISITA','STATUS'),
                                  qtd_linhas = 15,
                                  largura = 120,
                                  lar_min = 50)
        self.Tabela_Adocoes.Listagem.place(relx=0,rely=0,relwidth=0.982,relheight=0.8)
        self.Tabela_Adocoes.Barra_Y.place(relx=0.984 ,rely=0,relheight=0.835)
        self.Tabela_Adocoes.Barra_X.place(relx=0.0 ,rely=0.799,relwidth=0.982)
        
        #def Pegar_Infos(event):
        #    nodeId_1 = self.Tabela_Adocoes.Listagem.focus()
        #    id = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][0]
        
        #self.Tabela_Adocoes.Listagem.bind('<Double-1>',Pegar_Infos)
        
        self.mostrar_na_tabela_adocoes()
    
        # -------------------- BOTOES DE DECISAO -------------------------
        self.Frame_Decisoes_va = Frame(self.aba1)
        self.Frame_Decisoes_va.config(
            bg = '#086788'
        )
        self.Frame_Decisoes_va.place(relx=0,rely=0.80,relwidth=1,relheight=0.20)
        
        self.bt_Aprovar_adocao = Botoes(self.Frame_Decisoes_va,'Aprovar')
        self.bt_Aprovar_adocao.Botao.config(
            command = self.Aprovar_Adocao
        )
        self.bt_Aprovar_adocao.Botao.place(relx=0.35,rely=0.40,relwidth=0.15,relheight=0.25)
        
        self.bt_Reprovar_adocao = Botoes(self.Frame_Decisoes_va,'Reprovar')
        self.bt_Reprovar_adocao.Botao.config(
            command = self.Reprovar_Adocao
        )
        self.bt_Reprovar_adocao.Botao.place(relx=0.55,rely=0.40,relwidth=0.15,relheight=0.25)
    
    def atualiza_situacoes(self):
            self.situacoes_busca = BD.busca_situacoes_adocao()
            self.situacoes=[]
            for item in self.situacoes_busca:
                self.situacoes.append(item[0])
            self.et_situacao['values'] = self.situacoes
            
    def Aprovar_Adocao(self):
        nodeId_1 = self.Tabela_Adocoes.Listagem.focus()
        id_adocao = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][0]
        status_adocao = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][4]
        if status_adocao == 'Em Analise' or status_adocao == 'Reprovada' :
            BD.alterar_status_adocao(id_adocao,'Aprovada')
            messagebox.showinfo('Info Adoção',message='Adoção Aprovada com Sucesso!')
            self.mostrar_na_tabela_adocoes()
            self.atualiza_situacoes()
        elif status_adocao == 'Aprovada':
            messagebox.showinfo('Info Adoção',message='Essa Adoção Já Foi Aprovada!')
        else:
            messagebox.showinfo('Info Adoção',message='Essa Adoção Não Pode Ser Aprovada!')
         
    
    def Reprovar_Adocao(self):
        nodeId_1 = self.Tabela_Adocoes.Listagem.focus()
        id_adocao = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][0]
        status_adocao = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][4]
        if status_adocao == 'Em Analise':
            BD.alterar_status_adocao(id_adocao,'Reprovada')
            messagebox.showinfo('Info Adoção',message='Adoção Aprovada com Sucesso!')
            self.mostrar_na_tabela_adocoes()
            self.atualiza_situacoes()
        elif status_adocao == 'Reprovada':
            messagebox.showinfo('Info Adoção',message='Essa Adoção Já Foi Reprovada!')
        else:
            messagebox.showinfo('Info Adoção',message='Essa Adoção Não Pode Ser Reprovada!')
    
    def mostrar_na_tabela_adocoes(self,filtros={}): 
        self.Tabela_Adocoes.Listagem.delete(*self.Tabela_Adocoes.Listagem.get_children())
        self.Lista_Adocoes = BD.mostrar_adocoes(filtros)
        self.Tabela_Adocoes.Inserir(self.Lista_Adocoes)
        
    def Buscar_Adocao(self):
        busca = {}
        nome_pessoa = self.et_Nome_pess.Entrada.get()
        if nome_pessoa != '':
            busca['NOME_pessoa'] = nome_pessoa
            
        cod_pessoa = self.et_cod_pess.Entrada.get()
        if cod_pessoa != '':
            busca['FK_Cad_pessoa_COD_pessoa'] = cod_pessoa
            
        nome_pet = self.et_Nome_pet.Entrada.get()
        if nome_pet != '':
            busca['NOME_pet'] = nome_pet
            
        cod_pet = self.et_cod_pet.Entrada.get()
        if cod_pet != '':
            busca['FK_Pet_COD_pet'] = cod_pet

        situacao = self.situacao_selecionada.get()
        if situacao != '':
            busca['STATUS_adocao'] = situacao
            
        self.mostrar_na_tabela_adocoes(busca)
    
    def Limpar_Adocao(self):
        self.et_Nome_pess.Entrada.delete(0,END)
        self.et_cod_pess.Entrada.delete(0,END)
        self.et_Nome_pet.Entrada.delete(0,END)
        self.et_cod_pet.Entrada.delete(0,END)
        self.et_situacao.set('')
        
        self.mostrar_na_tabela_adocoes()
        
    # -------------------- ABA 2 - VERIFICAR VOLUNTARIOS ------------------
    def aba_verif_adotantes(self):
        
        self.Frame_Filtros_vv = Frame(self.aba2)
        self.Frame_Filtros_vv.config(
            bg = '#086788'
        )
        self.Frame_Filtros_vv.place(relx=0,rely=0,relwidth=1,relheight=0.30)
        
        self.Frame_Tabela_vv = Frame(self.aba2)
        self.Frame_Tabela_vv.config(
            bg = '#086788'
 
        )
        self.Frame_Tabela_vv.place(relx=0,rely=0.30,relwidth=1,relheight=0.50)
        
        self.Frame_Decisoes_vv = Frame(self.aba2)
        self.Frame_Decisoes_vv.config(
            bg = '#086788'
        )
        self.Frame_Decisoes_vv.place(relx=0,rely=0.80,relwidth=1,relheight=0.20)
    
    # -------------------- ABA 3 - VERIFICAR LARES TEMPORARIOS ------------------
    def aba_verif_lares(self):
    
        self.Frame_Filtros_vl = Frame(self.aba3)
        self.Frame_Filtros_vl.config(
            bg = '#086788'
        )
        self.Frame_Filtros_vl.place(relx=0,rely=0,relwidth=1,relheight=0.30)
        
        self.Frame_Tabela_vl = Frame(self.aba3)
        self.Frame_Tabela_vl.config(
            bg = '#086788'
 
        )
        self.Frame_Tabela_vl.place(relx=0,rely=0.30,relwidth=1,relheight=0.50)
        
        self.Frame_Decisoes_vl = Frame(self.aba3)
        self.Frame_Decisoes_vl.config(
            bg = '#086788'
        )
        self.Frame_Decisoes_vl.place(relx=0,rely=0.80,relwidth=1,relheight=0.20)
        
window = Tk()
Gerenciamento(window)