from tkinter import *
from PIL import Image, ImageTk
from Adocao import Adocao
from IMG import redimensionar
from cadPes import CadPes
from cadPet import CadPet
from cadCli import CadCli
from TabelaPets import VisualizarPets
from TabelaAdotantes import VisualizarPessoas
from login import Janela_Login
# -----------------------Class Button----------------------- #

class botoes:
    def __init__(self, container):
        self.bt = Button(container)
        self.bt.configure(
            bg='#C4C4C4',
            width=14,
            height=2,
            font=('Verdana', 18, 'bold')
        )
            
class Janela_Index:
    def __init__(self):
        # ------------------ Primeiro Chama a Tela de Login ---------------------- #
        self.abrir_login()
        
    def abrir_login(self):
        # ------------------ Cria nova tela da classe Login -------------------- #
        self.tela_login = Janela_Login()
        self.tela_login.botao_acesso.config(command=self.acessar_index)
        self.tela_login.entrada_senha.et.bind('<Return>',self.acessar_index)
        self.tela_login.root.mainloop()
        
    def acessar_index(self,event=None):
        
        # ------------------ Pega o nome e o privilegio do login e destroi a janela ----------- #
        self.nome,self.privilegio = self.tela_login.acesso_login()
        self.tela_login.root.destroy()
        
        # ------------------ Inicia a janela Index ------------------- #
        self.index = Tk()
        self.tela()
        self.inserir_elementos()
        self.index.mainloop()
    
    def voltar_login(self):
        # ------------------ Destroi a janela Index e chama novamente a funcao de abrir janela de login ---------- #
        self.index.destroy()
        self.abrir_login()
        
    def tela(self):
        self.index.title("Love Pet")
        self.index.geometry("1024x600")
        self.index.configure(bg="#086788")
        self.index.resizable(False, False)
        self.index.iconbitmap(default="Icones/Icone.ico")
    # --------------------Função sair-------------------- #

    def sairProg(self):
        self.index.destroy()
        #Janela_Login()
        
    # -------------------Funções para abrir as páginas-------------------#
    def Open_cadPes(self):
        CadPes(self.index)


    def Open_adoc(self):
        Adocao(self.index)


    def Open_geren(self):
        print('calma bb')


    def Open_cadPet(self):
        CadPet(self.index)


    def Open_tabPet(self):
        VisualizarPets(self.index,'ok','todos')


    def Open_cadCli(self):
        CadCli(self.index)

    def inserir_elementos(self):
        img = (Image.open('Icones\\sair.png'))
        self.img = redimensionar(img, 25, 25)
        
        # -----------------------Nome da empresa----------------------- #
        self.nome_empresa = Label(self.index)
        self.nome_empresa.configure(
            text="Love Pet",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 40, 'bold')
        )
        self.nome_empresa.place(x=378, y=30)
        
         # -----------------------Nome do usuario----------------------- #
        #nome = 'Evaldo'
        self.nome_usuario = Label(self.index)
        self.nome_usuario.configure(
            text="Olá, " + self.nome,
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana',10, 'bold')
        )
        self.nome_usuario.place(x=5, y=10)

        #----------------------- Botao Sair --------------------------#
        self.sair_botao = Button(self.index)
        self.sair_botao.configure(
            image=self.img,
            bg='#086788',
            width=30,
            height=30,
            relief=FLAT,
            command=self.voltar_login
        )
        self.sair_botao.place(x=978, y=10)

        #-----------Menu---------#
        #   --lado esquerdo--    #
        self.cadPes_but = botoes(self.index)
        self.cadPes_but.bt.configure(text='Cadastro', command=self.Open_cadPes)
        self.cadPes_but.bt.place(x=238, y=160)

        self.adoc_but = botoes(self.index)
        self.adoc_but.bt.configure(text='Adoção', command=self.Open_adoc)
        self.adoc_but.bt.place(x=238, y=260)

        self.geren_but = botoes(self.index)
        self.geren_but.bt.configure(text='Gerenciamento', command=self.Open_geren)
      
        #   --lado Direito--    #

        self.cadPet_but = botoes(self.index)
        self.cadPet_but.bt.configure(text='Cadastra Pet', command=self.Open_cadPet)
        self.cadPet_but.bt.place(x=538, y=160)

        self.tabPet_but = botoes(self.index)
        self.tabPet_but.bt.configure(text='Tabela de Pets', command=self.Open_tabPet)
        self.tabPet_but.bt.place(x=538, y=260)

        self.cadCli_but = botoes(self.index)
        self.cadCli_but.bt.configure(text='Cadastrar Clínicas', command=self.Open_cadCli)
        
        if self.privilegio == 'Administrador':
            self.geren_but.bt.place(x=238, y=360)
            self.cadCli_but.bt.place(x=538, y=360)
        else:
            self.cadCli_but.bt.place(x=380, y=360)
    
Janela_Index()