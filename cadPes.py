from tkinter import *
from tkinter import messagebox
import banco_de_dados as BD

# -----------------------Class Entry----------------------- #
class entrada:
    def __init__(self, container):
        self.et = Entry(container)
        self.et.configure(
            bg='#C4C4C4',
            fg='black',
            width=25,
            font=('Verdana', 12)
        )

# -----------------------Class Label----------------------- #
class textos:
    def __init__(self, container):
        self.lb = Label(container)
        self.lb.configure(
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 14, 'bold')
        )

class opcoes:
    def __init__(self,container,variavel,valor,texto):
        self.op = Radiobutton(container)
        self.op.configure(
                bg='#086788',
                fg='white',
                text= texto,
                font=('Verdana', 12, 'bold'),
                selectcolor="#086788",
                activebackground='#086788',
                activeforeground='white',
                variable=variavel,
                value= valor,
                )
# -----------------------Tela----------------------- #

class CadPes:
    def __init__(self, master):
        self.root = Toplevel(master)
        #self.root = master
        self.tela()
        self.adicionar_elementos()
        self.root.grab_set()
    
    def tela(self):
        self.root.title("Love Pet")
        self.root.geometry("600x700")
        self.root.configure(bg="#086788")
        self.root.resizable(False, False)
        
    def adicionar_elementos(self):
        #---- criando a Janela ----#
        self.janela = Frame(self.root)
        self.janela.configure(
            bg="#086788",
            highlightbackground="#086788",
            highlightthickness='0px'
        )
        self.janela.place(relx=0.0, rely=0.0,relwidth=1,relheight=1)
        
        self.frame_lbs = Frame(self.janela)
        self.frame_lbs.configure(
            bg="#086788",
        )
        self.frame_lbs.place(relx=0.05, rely=0.1,relwidth=0.35,relheight=0.95)
        
        self.frame_ent = Frame(self.janela)
        self.frame_ent.configure(
            bg="#086788",
        )
        self.frame_ent.place(relx=0.40, rely=0.1,relwidth=0.45,relheight=0.95)

    #---- titulo tela ----#
    
        self.nome_empresa = Label(self.janela)
        self.nome_empresa.configure(
            text="CADASTRO",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 24, 'bold')
        )
        self.nome_empresa.place(relx=0.32, rely=0.02)
    
    #---- Criando Label's da tela ----#
        self.nome_box = textos(self.frame_lbs)
        self.nome_box.lb.configure(text='Nome:')
        self.nome_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.cpf_box = textos(self.frame_lbs)
        self.cpf_box.lb.configure(text='CPF:')
        self.cpf_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.email_box = textos(self.frame_lbs)
        self.email_box.lb.configure(text='E-mail:')
        self.email_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.tel_box = textos(self.frame_lbs)
        self.tel_box.lb.configure(text='Telefone:')
        self.tel_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.espaco_box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_box.lb.pack(side=TOP, anchor='e',pady=17)
        
        self.rua_box = textos(self.frame_lbs)
        self.rua_box.lb.configure(text='Rua:')
        self.rua_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.numero_box = textos(self.frame_lbs)
        self.numero_box.lb.configure(text='N??mero:')
        self.numero_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.bairro_box = textos(self.frame_lbs)
        self.bairro_box.lb.configure(text='Bairro:')
        self.bairro_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.cidade_box = textos(self.frame_lbs)
        self.cidade_box.lb.configure(text='Cidade:')
        self.cidade_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.espaco_2box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_2box.lb.pack(side=TOP, anchor='e')

        self.tipo_box = textos(self.frame_lbs)
        self.tipo_box.lb.configure(text='Tipo de Cadastro:')
        self.tipo_box.lb.pack(side=TOP, anchor='e',pady=3)
        
        self.espaco_3box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_3box.lb.pack(side=TOP, anchor='e',pady=30)
        
        
        # ------------Endereco---------
        self.lbl_endereco = textos(self.janela)
        self.lbl_endereco.lb.configure(text='Endere??o')
        self.lbl_endereco.lb.place(relx=0.35, rely=0.33)
        #------------------------------
        
    #---- Criando Entry's da tela ----#
        self.nome_ent = entrada(self.frame_ent)
        self.nome_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.cpf_ent = entrada(self.frame_ent)
        self.cpf_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.email_ent = entrada(self.frame_ent)
        self.email_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.tel_ent = entrada(self.frame_ent)
        self.tel_ent.et.pack(side=TOP, anchor='w',pady=6)
        
        self.espaco_ent = textos(self.frame_ent) # -------------------- Espaco
        self.espaco_ent.lb.pack(side=TOP, anchor='w',pady=15)
        
        self.rua_ent = entrada(self.frame_ent)
        self.rua_ent.et.pack(side=TOP, anchor='w',pady=6)
        
        self.numero_ent = entrada(self.frame_ent)
        self.numero_ent.et.pack(side=TOP, anchor='w',pady=6)
        
        self.bairro_ent = entrada(self.frame_ent)
        self.bairro_ent.et.pack(side=TOP, anchor='w',pady=6)
        
        self.cidade_ent = entrada(self.frame_ent)
        self.cidade_ent.et.pack(side=TOP, anchor='w',pady=6)
        
        self.espaco_2ent = textos(self.frame_ent) # -------------------- Espaco
        self.espaco_2ent.lb.pack(side=TOP, anchor='w',pady=2)
        
        self.var = StringVar()
        self.tipo_voluntario = opcoes(self.frame_ent,self.var,'Voluntario','Volunt??rio')
        self.tipo_voluntario.op.pack(side=TOP, anchor='w')
        
        self.tipo_Adotante = opcoes(self.frame_ent,self.var,'Adotante','Adotante')
        self.tipo_Adotante.op.pack(side=TOP, anchor='w')
        
        self.tipo_Ambos = opcoes(self.frame_ent,self.var,'Ambos','Ambos')
        self.tipo_Ambos.op.pack(side=TOP, anchor='w')
        
        self.espaco_3ent = textos(self.frame_ent) # -------------------- Espaco
        self.espaco_3ent.lb.pack(side=TOP, anchor='w',pady=3)


    # -------- Botao de cadastrar ------------
        
        self.botao_cadastrar = Button(self.janela)
        self.botao_cadastrar.configure(
            text='Cadastrar',
            bg='#C4C4C4',
            font=('Verdana', 12, 'bold'),
            command=self.cadastrar
        )
        self.botao_cadastrar.place(relx=0.40,rely=0.90)
    
    def cadastrar(self):
        txt = ''
        self.Nome = self.nome_ent.et.get()
        if self.Nome == '':
            txt += 'Inserir o Nome!\n'
            
        self.CPF = self.cpf_ent.et.get()
        if self.CPF == '':
            txt += 'Inserir o CPF!\n'
            
        self.Email = self.email_ent.et.get()
        if self.Email == '':
            txt += 'Inserir o E-mail!\n'
            
        self.Telefone = self.tel_ent.et.get()
        if self.Telefone == '':
            txt += 'Inserir o Telefone!\n'
            
        self.Rua = self.rua_ent.et.get()
        if self.Rua == '':
            txt += 'Inserir a Rua!\n'
            
        self.Numero = self.numero_ent.et.get()
        if self.Numero == '':
            txt += 'Inserir o N??mero!\n'
            
        self.Bairro = self.bairro_ent.et.get()
        if self.Bairro == '':
            txt += 'Inserir o Bairro!\n'
            
        self.Cidade = self.cidade_ent.et.get()
        if self.Cidade == '':
            txt += 'Inserir a Cidade!\n'
            
        self.Tipo = self.var.get()
        if self.Tipo == '':
            txt += 'Selecionar o Tipo!\n'
        
        if txt == '':
            try:
                BD.Registrar_Pessoa(self.Nome,self.Rua,self.Numero,self.Bairro,self.Cidade,self.Telefone,self.Email,self.CPF,self.Tipo)
                messagebox.showinfo(title="Cadastro Info",message="Cadastrado com Sucesso!!\n")
                self.root.destroy()
            except:
                messagebox.showinfo(title="Cadastro Info",message="Houve Algum Problema!\n")
        else:
            messagebox.showinfo(title="Cadastro Info",message=txt)
        
#window = Tk()
#cadastro = CadPes(window)
#window.mainloop()
