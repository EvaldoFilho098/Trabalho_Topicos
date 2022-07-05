from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from IMG import redimensionar
from PIL import Image, ImageTk
from Tabelas import Tabelas
import banco_de_dados as BD
from cadPes import CadPes
#from IMG import redimensionar
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
        self.root = Toplevel(master)
        #self.root = master
        self.tela()
        self.inserir_frames()
        self.inserir_abas()
        #self.inserir_elementos()
        #self.root.mainloop()
        self.root.grab_set()

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
        #self.aba3 = Frame(self.Notebook, width=1000, height=460)

        self.aba1.pack(fill='both', expand=True)
        self.aba2.pack(fill='both', expand=True)
        #self.aba3.pack(fill='both', expand=True)

        # add frames to self.Notebook
        self.Notebook.add(self.aba1, text='Verificar Adoções')
        self.Notebook.add(self.aba2, text='Verificar Adotantes/Voluntários')
        #self.Notebook.add(self.aba3, text='Verificar Lares Temporários')
        
        self.aba_verif_adocao()
        self.aba_verif_adotantes()
        #self.aba_verif_lares()
    
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
        self.lb_Nome_pess_va = Textos(self.Frame_Filtros_va,'Nome Adotante:')
        self.lb_Nome_pess_va.Texto.place(relx=0.05,rely=0.30)
        
        self.lb_cod_pess_va = Textos(self.Frame_Filtros_va,'Código Adotante:')
        self.lb_cod_pess_va.Texto.place(relx=0.05,rely=0.5)
        
        self.lb_Nome_pet_va = Textos(self.Frame_Filtros_va,'Nome Pet:')
        self.lb_Nome_pet_va.Texto.place(relx=0.40,rely=0.30)
        
        self.lb_cod_pet_va = Textos(self.Frame_Filtros_va,'Código Pet:')
        self.lb_cod_pet_va.Texto.place(relx=0.40,rely=0.5)
        
        self.lb_situacao_va = Textos(self.Frame_Filtros_va,'Situação:')
        self.lb_situacao_va.Texto.place(relx=0.67,rely=0.30)
        
        #ENTRADAS
        self.et_Nome_pess_va = Entradas(self.Frame_Filtros_va)
        self.et_Nome_pess_va.Entrada.place(relx=0.185,rely=0.30)
        
        self.et_cod_pess_va = Entradas(self.Frame_Filtros_va)
        self.et_cod_pess_va.Entrada.place(relx=0.185,rely=0.5)
        
        self.et_Nome_pet_va = Entradas(self.Frame_Filtros_va)
        self.et_Nome_pet_va.Entrada.place(relx=0.495,rely=0.30)
        
        self.et_cod_pet_va = Entradas(self.Frame_Filtros_va)
        self.et_cod_pet_va.Entrada.place(relx=0.495,rely=0.5)
        
        
        self.situacao_selecionada_va = StringVar()
        self.et_situacao_va = ttk.Combobox(self.Frame_Filtros_va, textvariable=self.situacao_selecionada_va)            
        self.atualiza_situacoes_adocao()
        self.et_situacao_va['state'] = 'readonly'
        self.et_situacao_va.place(relx=0.75,rely=0.30)
        
        #BOTAO DE PESQUISAR
        self.bt_Buscar_va = Botoes(self.Frame_Filtros_va,'Buscar')
        self.bt_Buscar_va.Botao.config(command=self.Buscar_Adocao)
        self.bt_Buscar_va.Botao.place(relx=0.35,rely=0.85,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.bt_Limpar_va = Botoes(self.Frame_Filtros_va,'Limpar')
        self.bt_Limpar_va.Botao.config(command=self.Limpar_Adocao)
        self.bt_Limpar_va.Botao.place(relx=0.55,rely=0.85,relwidth=0.15,relheight=0.15)

        
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
    
    def atualiza_situacoes_adocao(self):
            self.situacoes_busca_va = BD.busca_situacoes_adocao()
            self.situacoes_va=[]
            for item in self.situacoes_busca_va:
                self.situacoes_va.append(item[0])
            self.et_situacao_va['values'] = self.situacoes_va
        
    def mudar_status_pet_(self,node,status):
        id_adocao = self.Tabela_Adocoes.Listagem.item(node)['values'][0]
        for item in self.Lista_Adocoes_ids:
            if item[0] == id_adocao:
                self.id_pet = item[2]
        
        BD.alterar_status_pet(self.id_pet,status)
        
    def Aprovar_Adocao(self):
        nodeId_1 = self.Tabela_Adocoes.Listagem.focus()
        id_adocao = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][0]
        status_adocao = self.Tabela_Adocoes.Listagem.item(nodeId_1)['values'][4]
        if status_adocao == 'Em Analise' or status_adocao == 'Reprovada' :
            BD.alterar_status_adocao(id_adocao,'Aprovada')
            self.mudar_status_pet_(nodeId_1,'Adotado')
            messagebox.showinfo('Info Adoção',message='Adoção Aprovada com Sucesso!')
            self.mostrar_na_tabela_adocoes()
            self.atualiza_situacoes_adocao()
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
            self.mudar_status_pet_(nodeId_1,'Liberado')
            messagebox.showinfo('Info Adoção',message='Adoção Aprovada com Sucesso!')
            self.mostrar_na_tabela_adocoes()
            self.atualiza_situacoes_adocao()
        elif status_adocao == 'Reprovada':
            messagebox.showinfo('Info Adoção',message='Essa Adoção Já Foi Reprovada!')
        else:
            messagebox.showinfo('Info Adoção',message='Essa Adoção Não Pode Ser Reprovada!')
    
    def mostrar_na_tabela_adocoes(self,filtros={}): 
        self.Tabela_Adocoes.Listagem.delete(*self.Tabela_Adocoes.Listagem.get_children())
        self.Lista_Adocoes,self.Lista_Adocoes_ids = BD.mostrar_adocoes(filtros)
        self.Tabela_Adocoes.Inserir(self.Lista_Adocoes)
        
    def Buscar_Adocao(self):
        busca = {}
        nome_pessoa = self.et_Nome_pess_va.Entrada.get()
        if nome_pessoa != '':
            busca['NOME_pessoa'] = nome_pessoa
            
        cod_pessoa = self.et_cod_pess_va.Entrada.get()
        if cod_pessoa != '':
            busca['FK_Cad_pessoa_COD_pessoa'] = cod_pessoa
            
        nome_pet = self.et_Nome_pet_va.Entrada.get()
        if nome_pet != '':
            busca['NOME_pet'] = nome_pet
            
        cod_pet = self.et_cod_pet_va.Entrada.get()
        if cod_pet != '':
            busca['FK_Pet_COD_pet'] = cod_pet

        situacao = self.situacao_selecionada_va.get()
        if situacao != '':
            busca['STATUS_adocao'] = situacao
            
        self.mostrar_na_tabela_adocoes(busca)
    
    def Limpar_Adocao(self):
        self.et_Nome_pess_va.Entrada.delete(0,END)
        self.et_cod_pess_va.Entrada.delete(0,END)
        self.et_Nome_pet_va.Entrada.delete(0,END)
        self.et_cod_pet_va.Entrada.delete(0,END)
        self.et_situacao_va.set('')
        
        self.mostrar_na_tabela_adocoes()
        
    # -------------------- ABA 2 - VERIFICAR VOLUNTARIOS ------------------
    def aba_verif_adotantes(self):
        
        # ---------------------------- FILTROS ---------------------------
        self.Frame_Filtros_vv = Frame(self.aba2)
        self.Frame_Filtros_vv.config(
            bg = '#086788'
        )
        self.Frame_Filtros_vv.place(relx=0,rely=0,relwidth=1,relheight=0.30)
        
        self.lb_Filtros_vv = Textos(self.Frame_Filtros_vv,'Filtros','#086788','white')
        self.lb_Filtros_vv.Texto.config(font=('verdana',14,'bold'))
        self.lb_Filtros_vv.Texto.place(relx = 0.48,rely=0)
        
        
        img = (Image.open('Icones\\atualizar.png'))
        self.Img_Atualizar= redimensionar(img,20,20)
        self.botao_atualizar_vv = Button(self.Frame_Filtros_vv,image=self.Img_Atualizar)
        self.botao_atualizar_vv.config(command=self.mostrar_na_tabela_voluntarios,bg='#C4C4C4')
        self.botao_atualizar_vv.place(relx=0.97,rely=0.9,relheight=0.1,relwidth=0.03)
        
        #LABELS
        self.lb_Nome_pess_vv = Textos(self.Frame_Filtros_vv,'Nome Adotante:')
        self.lb_Nome_pess_vv.Texto.place(relx=0.25,rely=0.30)
        
        self.lb_cod_pess_vv = Textos(self.Frame_Filtros_vv,'Código Adotante:')
        self.lb_cod_pess_vv.Texto.place(relx=0.25,rely=0.5)
        
        self.lb_tipo_vv = Textos(self.Frame_Filtros_vv,'Tipo:')
        self.lb_tipo_vv.Texto.place(relx=0.57,rely=0.30)
        
        #ENTRADAS
        self.et_Nome_pess_vv = Entradas(self.Frame_Filtros_vv)
        self.et_Nome_pess_vv.Entrada.place(relx=0.385,rely=0.30)
        
        self.et_cod_pess_vv = Entradas(self.Frame_Filtros_vv)
        self.et_cod_pess_vv.Entrada.place(relx=0.385,rely=0.5)
        
        self.tipo_selecionado_vv = StringVar()
        self.et_tipo_vv = ttk.Combobox(self.Frame_Filtros_vv, textvariable=self.tipo_selecionado_vv)            
        self.atualiza_situacoes_voluntarios()
        self.et_tipo_vv['state'] = 'readonly'
        self.et_tipo_vv.place(relx=0.65,rely=0.30)
        
        #BOTAO DE PESQUISAR
        self.bt_Buscar_vv = Botoes(self.Frame_Filtros_vv,'Buscar')
        self.bt_Buscar_vv.Botao.config(command=self.Buscar_Voluntario)
        self.bt_Buscar_vv.Botao.place(relx=0.35,rely=0.85,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.bt_Limpar_vv = Botoes(self.Frame_Filtros_vv,'Limpar')
        self.bt_Limpar_vv.Botao.config(command=self.Limpar_Voluntario)
        self.bt_Limpar_vv.Botao.place(relx=0.55,rely=0.85,relwidth=0.15,relheight=0.15)

        
        # -------------------- TABELA --------------------------
        self.Frame_Tabela_vv = Frame(self.aba2)
        self.Frame_Tabela_vv.config(
            bg = '#086788'
        )
        self.Frame_Tabela_vv.place(relx=0,rely=0.30,relwidth=1,relheight=0.60)
        
        
        self.Tabela_Voluntarios = Tabelas(self.Frame_Tabela_vv,
                                  colunas = ('ID','NOME','CPF','E-MAIL','ENDEREÇO','TELEFONE','TIPO'),
                                  qtd_linhas = 15,
                                  largura = 120,
                                  lar_min = 50)
        self.Tabela_Voluntarios.Listagem.place(relx=0,rely=0,relwidth=0.982,relheight=0.8)
        self.Tabela_Voluntarios.Barra_Y.place(relx=0.984 ,rely=0,relheight=0.835)
        self.Tabela_Voluntarios.Barra_X.place(relx=0.0 ,rely=0.799,relwidth=0.982)
        
        self.mostrar_na_tabela_voluntarios()
    
        # -------------------- BOTOES DE DECISAO -------------------------
        self.Frame_Decisoes_vv = Frame(self.aba2)
        self.Frame_Decisoes_vv.config(
            bg = '#086788'
        )
        self.Frame_Decisoes_vv.place(relx=0,rely=0.80,relwidth=1,relheight=0.20)
        
        self.bt_Adicionar_Voluntario = Botoes(self.Frame_Decisoes_vv,'Adicionar')
        self.bt_Adicionar_Voluntario.Botao.config(
            command = self.Adicionar_Voluntario
        )
        self.bt_Adicionar_Voluntario.Botao.place(relx=0.45,rely=0.40,relwidth=0.15,relheight=0.25)
        
        #self.bt_Remover_Voluntario = Botoes(self.Frame_Decisoes_vv,'Remover')
        #self.bt_Remover_Voluntario.Botao.config(
        #    command = self.Remover_Voluntario
        #)
        #self.bt_Remover_Voluntario.Botao.place(relx=0.55,rely=0.40,relwidth=0.15,relheight=0.25)
    
    def Adicionar_Voluntario(self):
        CadPes(self.root)
    
    def Remover_Voluntario(self):
        nodeId_1 = self.Tabela_Voluntarios.Listagem.focus()
        id_adotante = self.Tabela_Voluntarios.Listagem.item(nodeId_1)['values'][0]
        BD.remover_adotante(id_adotante)
        messagebox.showinfo('Deletar Adotante/Voluntário','Adotante/Voluntário Removido!')
        self.mostrar_na_tabela_voluntarios()
    
    def atualiza_situacoes_voluntarios(self):
        self.tipo_busca_vv = BD.busca_situacoes_voluntarios()
        self.tipos_vv=[]
        for item in self.tipo_busca_vv:
            self.tipos_vv.append(item[0])
        self.et_tipo_vv['values'] = self.tipos_vv
    
    def mostrar_na_tabela_voluntarios(self,filtros={}): 
        self.Tabela_Voluntarios.Listagem.delete(*self.Tabela_Voluntarios.Listagem.get_children())
        self.Lista_Voluntarios = BD.mostrar_adotantes(filtros)
        self.Tabela_Voluntarios.Inserir(self.Lista_Voluntarios)
        self.atualiza_situacoes_voluntarios()
    
    def Buscar_Voluntario(self):
        busca = {}
        nome_pessoa = self.et_Nome_pess_vv.Entrada.get()
        if nome_pessoa != '':
            busca['NOME_pessoa'] = nome_pessoa
            
        cod_pessoa = self.et_cod_pess_vv.Entrada.get()
        if cod_pessoa != '':
            busca['COD_pessoa'] = cod_pessoa
            
        tipo = self.tipo_selecionado_vv.get()
        if tipo != '':
            busca['TIPO_CAD_pessoa'] = tipo
            
        self.mostrar_na_tabela_voluntarios(busca)
    
    def Limpar_Voluntario(self):
        self.et_Nome_pess_vv.Entrada.delete(0,END)
        self.et_cod_pess_vv.Entrada.delete(0,END)
        self.et_tipo_vv.set('')
        
        self.mostrar_na_tabela_voluntarios()
        
    # -------------------- ABA 3 - VERIFICAR LARES TEMPORARIOS ------------------
    def aba_verif_lares(self):
    
        # ---------------------------- FILTROS ---------------------------
        self.Frame_Filtros_vl = Frame(self.aba3)
        self.Frame_Filtros_vl.config(
            bg = '#086788'
        )
        self.Frame_Filtros_vl.place(relx=0,rely=0,relwidth=1,relheight=0.30)
        
        self.lb_Filtros_vl = Textos(self.Frame_Filtros_vl,'Filtros','#086788','white')
        self.lb_Filtros_vl.Texto.config(font=('verdana',14,'bold'))
        self.lb_Filtros_vl.Texto.place(relx = 0.48,rely=0)
        
        #LABELS
        self.lb_Nome_pess_vl = Textos(self.Frame_Filtros_vl,'Nome Adotante:')
        self.lb_Nome_pess_vl.Texto.place(relx=0.05,rely=0.30)
        
        self.lb_cod_pess_vl = Textos(self.Frame_Filtros_vl,'Código Adotante:')
        self.lb_cod_pess_vl.Texto.place(relx=0.05,rely=0.5)
        
        self.lb_Nome_pet_vl = Textos(self.Frame_Filtros_vl,'Nome Pet:')
        self.lb_Nome_pet_vl.Texto.place(relx=0.40,rely=0.30)
        
        self.lb_cod_pet_vl = Textos(self.Frame_Filtros_vl,'Código Pet:')
        self.lb_cod_pet_vl.Texto.place(relx=0.40,rely=0.5)
        
        self.lb_situacao_vl = Textos(self.Frame_Filtros_vl,'Situação:')
        self.lb_situacao_vl.Texto.place(relx=0.67,rely=0.30)
        
        #ENTRADAS
        self.et_Nome_pess_vl = Entradas(self.Frame_Filtros_vl)
        self.et_Nome_pess_vl.Entrada.place(relx=0.185,rely=0.30)
        
        self.et_cod_pess_vl = Entradas(self.Frame_Filtros_vl)
        self.et_cod_pess_vl.Entrada.place(relx=0.185,rely=0.5)
        
        self.et_Nome_pet_vl = Entradas(self.Frame_Filtros_vl)
        self.et_Nome_pet_vl.Entrada.place(relx=0.495,rely=0.30)
        
        self.et_cod_pet_vl = Entradas(self.Frame_Filtros_vl)
        self.et_cod_pet_vl.Entrada.place(relx=0.495,rely=0.5)
        
        
        self.situacao_selecionada_vl = StringVar()
        self.et_situacao_vl = ttk.Combobox(self.Frame_Filtros_vl, textvariable=self.situacao_selecionada_vl)            
        #self.atualiza_situacoes_adocao()
        self.et_situacao_vl['state'] = 'readonly'
        self.et_situacao_vl.place(relx=0.75,rely=0.30)
        
        #BOTAO DE PESQUISAR
        self.bt_Buscar_vl = Botoes(self.Frame_Filtros_vl,'Buscar')
        self.bt_Buscar_vl.Botao.config(command=self.Buscar_Adocao)
        self.bt_Buscar_vl.Botao.place(relx=0.35,rely=0.85,relwidth=0.15,relheight=0.15)
        
        #BOTAO DE LIMPAR FILTROS
        self.bt_Limpar_vl = Botoes(self.Frame_Filtros_vl,'Limpar')
        self.bt_Limpar_vl.Botao.config(command=self.Limpar_Adocao)
        self.bt_Limpar_vl.Botao.place(relx=0.55,rely=0.85,relwidth=0.15,relheight=0.15)

        
        # -------------------- TABELA --------------------------
        self.Frame_Tabela_vl = Frame(self.aba3)
        self.Frame_Tabela_vl.config(
            bg = '#086788'
        )
        self.Frame_Tabela_vl.place(relx=0,rely=0.30,relwidth=1,relheight=0.60)
        
        
        self.Tabela_Lares = Tabelas(self.Frame_Tabela_vl,
                                  colunas = ('ID','NOME ADOTANTE','NOME PET','DATA DE VISITA','STATUS'),
                                  qtd_linhas = 15,
                                  largura = 120,
                                  lar_min = 50)
        self.Tabela_Lares.Listagem.place(relx=0,rely=0,relwidth=0.982,relheight=0.8)
        self.Tabela_Lares.Barra_Y.place(relx=0.984 ,rely=0,relheight=0.835)
        self.Tabela_Lares.Barra_X.place(relx=0.0 ,rely=0.799,relwidth=0.982)
        
        #self.mostrar_na_tabela_adocoes()
    
        # -------------------- BOTOES DE DECISAO -------------------------
        self.Frame_Decisoes_vl = Frame(self.aba3)
        self.Frame_Decisoes_vl.config(
            bg = '#086788'
        )
        self.Frame_Decisoes_vl.place(relx=0,rely=0.80,relwidth=1,relheight=0.20)
        
        self.bt_Aprovar_adocao = Botoes(self.Frame_Decisoes_vl,'Aprovar')
        self.bt_Aprovar_adocao.Botao.config(
            command = self.Aprovar_Adocao
        )
        self.bt_Aprovar_adocao.Botao.place(relx=0.35,rely=0.40,relwidth=0.15,relheight=0.25)
        
        self.bt_Reprovar_adocao = Botoes(self.Frame_Decisoes_vl,'Reprovar')
        self.bt_Reprovar_adocao.Botao.config(
            command = self.Reprovar_Adocao
        )
        self.bt_Reprovar_adocao.Botao.place(relx=0.55,rely=0.40,relwidth=0.15,relheight=0.25)
        
#window = Tk()
#Gerenciamento(window)