from tkinter import *
from tkinter import messagebox
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


class Janela_Login:
    def __init__(self):
        self.root = Tk()
        #self.root = master
        self.tela()
        self.menus()
        self.inserir_elementos()
        #self.root.mainloop()

    def tela(self):
        self.root.title("Login")
        self.root.geometry("1024x600")
        self.root.configure(bg="#086788")
        self.root.resizable(False, False)
        self.root.iconbitmap(default="Icones/Icone.ico")

    # -----------------------Menus----------------------- #
    def menus(self):
        self.menubar = Menu(self.root)
        self.Ajuda = Menu(self.menubar)
        self.Ajuda.configure(tearoff=0)
        self.menubar.add_cascade(label="Ajuda", menu=self.Ajuda)
        self.Ajuda.add_command(label="Sobre")
        self.root.config(menu=self.menubar)

    # -----------------------Elementos de acesso----------------------- #
    def inserir_elementos(self):
        
        self.frame_1 = Frame(self.root)
        self.frame_1.config(bg="#086788")
        self.frame_1.pack(side=TOP,anchor='center')
        
        # -----------------------Login----------------------- #
        self.text_box = Label(self.frame_1)
        self.text_box.configure(
            text="Login:",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 35, 'bold')
        )
        self.text_box.pack(side=TOP, padx=10, pady=60, anchor='center')

        # -----------------------e-mail----------------------- #
        self.email_box = Label(self.frame_1)
        self.email_box.configure(
            text="E-mail:",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 25, 'bold')
        )
        self.email_box.pack(side=TOP, anchor='center')

        self.entrada_email = entrada(self.frame_1)
        self.entrada_email.et.pack(side=TOP, padx=10, pady=10, anchor='center')

        # -----------------------Senha----------------------- #
        self.senha_box = Label(self.frame_1)
        self.senha_box.configure(
            text="Senha:",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 25, 'bold')
        )
        self.senha_box.pack(side=TOP, anchor='center')

        self.entrada_senha = entrada(self.frame_1)
        self.entrada_senha.et.configure(show='*')
        
        self.entrada_senha.et.pack(side=TOP, padx=10, pady=10, anchor='center')

        # -----------------------Acesso----------------------- #
        self.botao_acesso = Button(self.frame_1)
        self.botao_acesso.configure(
            text='Acessar',
            bg='#C4C4C4',
            fg='black',
            font=('Verdana', 20, 'bold'),
            width=7,
            height=1,
            activebackground='black',
            #command=self.acesso_login
        )
        self.botao_acesso.pack(side=TOP, padx=10, pady=10, anchor='center')

        # ------------------- Registrar ---------------------- #
        self.registrar = Button(self.frame_1)
        self.registrar.configure(
            text='Registrar',
            bg='#086788',
            fg='white',
            font=('Verdana', 9),
            width=7,
            activebackground='white',
            relief=FLAT,
            command=self.login_registro
            
        )
        self.registrar.pack(side=TOP, anchor='center')
        
        img = (Image.open('sair.png'))
        self.img = redimensionar(img, 25, 25)
        
        self.sair_botao = Button(self.frame_1)
        self.sair_botao.configure(
            image=self.img,
            bg='#086788',
            width=30,
            height=30,
            relief=FLAT,
            command=self.root.destroy
        )
        self.sair_botao.pack(side=TOP,pady=20, anchor='center')

    def login_registro(self,event=None):
        
        # ---------------------- Tela de Login Aministrador ------------------ #
        self.admin = Toplevel(self.root)
        self.admin.title("ACESSO RESTRITO")
        self.admin.geometry("330x135")
        self.admin.configure(bg="#086788")
        self.admin.resizable(False, False)
        self.admin.iconbitmap(default="Icones/Icone.ico")
        self.admin.grab_set()
        
        # ----------------------- Frames Para Posicionamento ----------------- #
        self.frame_lbls = Frame(self.admin)
        self.frame_lbls.configure(
            bg="#086788"
        )
        self.frame_lbls.place(relx=0.0,rely=0.22,relheight=0.7,relwidth=0.45)
        
        self.frame_ents = Frame(self.admin)
        self.frame_ents.configure(
            bg="#086788"
        )
        self.frame_ents.place(relx=0.50,rely=0.22,relheight=0.7,relwidth=0.4)
        
        self.frame_botao = Frame(self.admin)
        self.frame_botao.configure(
            bg="#086788"
        )
        self.frame_botao.place(relx=0.45,rely=0.75)
        
        # ----------------------- Login --------------------------- #
        self.lbl_login_admin = Label(self.admin)
        self.lbl_login_admin.configure(
            text="Login de Administrador",
            bg="#086788",
            fg="white",
            font=("verdana",12,'bold')
        )
        self.lbl_login_admin.pack(side=TOP,anchor='center',pady=5)
        
        # ----------------------- Email --------------------------- #
        self.lbl_email_admin = Label(self.frame_lbls)
        self.lbl_email_admin.configure(
            text="Email:",
            bg="#086788",
            fg="white",
            font=("verdana",10)
        )
        self.lbl_email_admin.pack(side=TOP,anchor='e',pady=5)

        self.entrada_login_admin = Entry(self.frame_ents)
        self.entrada_login_admin.pack(side=TOP,anchor='w',pady=5)
        
        # ----------------------- Senha --------------------------- #
        self.lbl_senha_admin = Label(self.frame_lbls)
        self.lbl_senha_admin.configure(
            text="Senha:",
            bg="#086788",
            fg="white",
            font=("verdana",10)
        )
        self.lbl_senha_admin.pack(side=TOP,anchor='e',pady=5)

        self.entrada_senha_admin = Entry(self.frame_ents,show='*')
        self.entrada_senha_admin.bind('<Return>',self.tela_registro)
        self.entrada_senha_admin.pack(side=TOP,anchor='w',pady=5)
        
        # ----------------------- Entrar ------------------------- #
        self.bt_entrar_admin = Button(self.frame_botao)
        self.bt_entrar_admin.configure(
            text='Entrar',
            bg='#C4C4C4',
            fg='black',
            font=('Verdana', 9),
            width=7,
            activebackground='white',
            #relief=FLAT,
            command=self.tela_registro
            
        )
        self.bt_entrar_admin.pack(side=TOP, anchor='center')
    
        
    def tela_registro(self,event=None):
        #Verificar se tem este usuário 
        login = self.entrada_login_admin.get()
        senha = self.entrada_senha_admin.get()
        
        verifica = BD.Verificar_Admin(login,senha)
        
        if verifica != None:
            #print(verifica)
            #Se tiver o usuario, destroi a janela de login adminstrador
            self.admin.destroy()
            #Retira a configuração inicial da tela
            self.frame_1.pack_forget()
            #self.frame_1.place(x=5000)
            
            # ---------------------- Novo frame para posicionamento ----------------- #
            self.frame_2 = Frame(self.root)
            self.frame_2.config(bg="#086788")
            self.frame_2.place(relx=0,rely=0,relwidth=1, relheight=1)
            
            # -----------------------Novo Funcionario----------------------- #
            self.text_box = Label(self.frame_2)
            self.text_box.configure(
                text="Novo Funcionário",
                bg='#086788',
                fg='#FFFFFF',
                font=('Verdana', 35, 'bold')
            )
            self.text_box.pack(side=TOP, pady=50, anchor='center')
            
            # ----------------------- Frames de Posicionamento --------------------#
            self.frame_lbls_reg = Frame(self.frame_2)
            self.frame_lbls_reg.config(
                bg="#086788",
                )
            self.frame_lbls_reg.place(relx=0.0,rely=0.3,relwidth=0.45,relheight=0.50)
            
            self.frame_ent_reg = Frame(self.frame_2)
            self.frame_ent_reg.config(
                bg="#086788",
                )
            self.frame_ent_reg.place(relx=0.45,rely=0.3,relwidth=0.5,relheight=0.50)
            
            self.frame_botao_reg = Frame(self.frame_2)
            self.frame_botao_reg.configure(
                bg="#086788",
                )
            self.frame_botao_reg.place(relx=0.0,rely=0.80,relwidth=1,relheight=0.20)
            
            # -----------------------Login----------------------- #
            self.login_box = Label(self.frame_lbls_reg)
            self.login_box.configure(
                text="Nome:",
                bg='#086788',
                fg='#FFFFFF',
                font=('Verdana', 16, 'bold')
            )
            self.login_box.pack(side=TOP, padx=10, pady=10, anchor='e')

            self.entrada_login_reg = Entry(self.frame_ent_reg)
            self.entrada_login_reg.configure(
                font=('Verdana', 16),
                width=25
            )
            self.entrada_login_reg.pack(side=TOP, padx=10, pady=10, anchor='w')
            
            # -----------------------e-mail----------------------- #
            self.email_box = Label(self.frame_lbls_reg)
            self.email_box.configure(
                text="E-mail:",
                bg='#086788',
                fg='#FFFFFF',
                font=('Verdana', 16, 'bold')
            )
            self.email_box.pack(side=TOP, padx=10, pady=10, anchor='e')

            self.entrada_email_reg = Entry(self.frame_ent_reg)
            self.entrada_email_reg.configure(
                font=('Verdana', 16),
                width=25
            )
            self.entrada_email_reg.pack(side=TOP, padx=10, pady=10, anchor='w')

            # -----------------------Senha----------------------- #
            self.senha_box = Label(self.frame_lbls_reg)
            self.senha_box.configure(
                text="Senha:",
                bg='#086788',
                fg='#FFFFFF',
                font=('Verdana', 16, 'bold')
            )
            self.senha_box.pack(side=TOP, padx=10, pady=10, anchor='e')

            self.entrada_senha_reg = Entry(self.frame_ent_reg)
            self.entrada_senha_reg.configure(
                show='*',
                font=('Verdana', 14),
                width=27
            )
            self.entrada_senha_reg.pack(side=TOP, padx=10, pady=10, anchor='w')
            
            # -----------------------Tipo User---------------------- #
            self.tipo_user_lbl = Label(self.frame_lbls_reg)
            self.tipo_user_lbl.configure(
                text="Acesso de :",
                bg='#086788',
                fg='#FFFFFF',
                font=('Verdana', 16, 'bold')
            )
            self.tipo_user_lbl.pack(side=TOP, padx=10, pady=10, anchor='e')

            self.var = IntVar()
            
            self.tipo_user_rdb = Radiobutton(self.frame_ent_reg)
            self.tipo_user_rdb.configure(
                bg='#086788',
                fg='white',
                text='Administrador',
                font=('Verdana', 12, 'bold'),
                selectcolor="#086788",
                activebackground='#086788',
                activeforeground='white',
                variable=self.var,
                value= 1,

            )
            self.tipo_user_rdb.pack(side=TOP, padx=5, pady=5 , anchor='w')
            
            self.tipo_user_rdb = Radiobutton(self.frame_ent_reg)
            self.tipo_user_rdb.configure(
                bg='#086788',
                fg='white',
                text='Funcionário',
                font=('Verdana', 12, 'bold'),
                selectcolor="#086788",
                activebackground='#086788',
                activeforeground='white',
                variable=self.var,
                value= 2,

            )
            self.tipo_user_rdb.pack(side=TOP, padx=5, pady=5 , anchor='w')
            
            # -----------------------Acesso----------------------- #
            self.botao_registrar = Button(self.frame_botao_reg)
            self.botao_registrar.configure(
                text='Registrar',
                bg='#C4C4C4',
                fg='black',
                font=('Verdana', 12, 'bold'),
                width=7,
                height=1,
                activebackground='black',
                command= self.realizar_registro
            )
            self.botao_registrar.pack(side=TOP, padx=10, pady=10, anchor='center')
            
            # -----------------------Voltar----------------------- #
            self.botao_voltar = Button(self.frame_botao_reg)
            self.botao_voltar.configure(
                text='Voltar',
                bg='#086788',
                fg='white',
                font=('Verdana', 10, 'bold'),
                width=7,
                height=1,
                activebackground='#086788',
                command= self.voltar_inicio,
                relief=FLAT
            )
            self.botao_voltar.pack(side=TOP, padx=10, pady=10, anchor='center')
        else:
            messagebox.showinfo(title="Login Info",message="Login Administrador Inválido!\n")
        
    def voltar_inicio(self):
        # Destruir Tela de Registro
        self.frame_2.destroy()
        # Voltar Configuração Inicial
        self.frame_1.pack(side=TOP)
        
    def realizar_registro(self,event=None):
        
        txt = ""
        login = self.entrada_login_reg.get()
        if login == '':
            txt += 'Login Inválido!\n'
        email = self.entrada_email_reg.get()
        if email == '':
            txt += 'Email Inválido!\n'
        senha = self.entrada_senha_reg.get()
        if senha == '':
            txt += 'Senha Inválido!\n'
        usuario = self.var.get()
        if usuario == 0:
            txt += 'Selecione um Tipo de Acesso!\n'
        elif usuario == 1:
            usuario = 'Administrador'
        elif usuario == 2:
            usuario = 'Funcionario'
        
        if txt == "":
            erro = False
            
            try:
                BD.Registrar_Usuario(login,email,senha,usuario)
                
                messagebox.showinfo(title="Login Info", message="Cadastrado Com Sucesso!\n")
            except:
                erro = True
                messagebox.showinfo(title="Login Info",message="Login Inválido!\n")
            
            if not erro:
                # Destruir Tela de Registro
                self.frame_2.destroy()
                # Voltar Configuração Inicial
                self.frame_1.pack(side=TOP)
        else:
            messagebox.showinfo(title="Login Info",message=txt)
    
    # -----------------------Função Get----------------------- #   
    def acesso_login(self):
        get_senha = self.entrada_senha.et.get()
        get_email = self.entrada_email.et.get()
        
        verifica = BD.Verificar_Login(get_email,get_senha)
        
        if verifica != None:
            return (verifica[1],verifica[4])
        else:
            messagebox.showinfo(title="Login Info",message="LOGIN INVÁLIDO")
            
#Janela_Login()