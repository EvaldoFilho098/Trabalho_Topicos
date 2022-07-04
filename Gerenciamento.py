from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import banco_de_dados as BD
from IMG import redimensionar
#from index import *

# -----------------------Class Entry----------------------- #
class entrada:
    def __init__(self, container):
        self.et = Entry(container)
        self.et.configure(
            bg='#C4C4C4',
            fg='black',
            width=20,
            font=('Verdana', 20)
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
        self.Frame_Filtros_va = Frame(self.aba1)
        self.Frame_Filtros_va.config(
            bg = '#086788'
        )
        self.Frame_Filtros_va.place(relx=0,rely=0,relwidth=1,relheight=0.30)
        
        self.Frame_Tabela_va = Frame(self.aba1)
        self.Frame_Tabela_va.config(
            bg = '#086788'
        )
        self.Frame_Tabela_va.place(relx=0,rely=0.30,relwidth=1,relheight=0.50)
        
        self.Frame_Decisoes_va = Frame(self.aba1)
        self.Frame_Decisoes_va.config(
            bg = '#086788'
        )
        self.Frame_Decisoes_va.place(relx=0,rely=0.80,relwidth=1,relheight=0.20)
        
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