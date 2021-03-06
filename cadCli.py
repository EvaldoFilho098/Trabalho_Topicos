from tkinter import filedialog as dlg, messagebox
from tkinter import *
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
    def __init__(self,container,variavel,texto):
        self.op = Checkbutton(container)
        self.op.configure(
                bg='#086788',
                fg='white',
                text= texto,
                font=('Verdana', 12, 'bold'),
                selectcolor="#086788",
                activebackground='#086788',
                activeforeground='white',
                variable=variavel,
                )
# -----------------------Tela----------------------- #

class CadCli:
    def __init__(self, master):
        #self.root = Toplevel(master)
        self.root = master
        self.tela()
        self.adicionar_elementos()
        self.root.mainloop()
        #self.root.grab_set()
    
    def tela(self):
        self.root.title("Love Pet")
        self.root.geometry("600x300")
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
        self.frame_lbs.place(relx=0.05, rely=0.2,relwidth=0.35,relheight=0.95)
        
        self.frame_ent = Frame(self.janela)
        self.frame_ent.configure(
            bg="#086788",
        )
        self.frame_ent.place(relx=0.40, rely=0.2,relwidth=0.45,relheight=0.95)

    #---- titulo tela ----#
    
        self.nome_empresa = Label(self.janela)
        self.nome_empresa.configure(
            text="CADASTRAR CL??NICA",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 24, 'bold')
        )
        self.nome_empresa.place(relx=0.18, rely=0.02)
    
    #---- Criando Label's da tela ----#
        self.nome_box = textos(self.frame_lbs)
        self.nome_box.lb.configure(text='Nome:')
        self.nome_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.cnpj_box = textos(self.frame_lbs)
        self.cnpj_box.lb.configure(text='CNPJ:')
        self.cnpj_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.telefone_box = textos(self.frame_lbs)
        self.telefone_box.lb.configure(text='Telefone:')
        self.telefone_box.lb.pack(side=TOP, anchor='e',pady=2)
 
        self.endereco_box = textos(self.frame_lbs)
        self.endereco_box.lb.configure(text='Endere??o:')
        self.endereco_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.espaco_2box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_2box.lb.pack(side=TOP, anchor='e')
        
    #---- Criando Entry's da tela ----#
        self.nome_ent = entrada(self.frame_ent)
        self.nome_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.cnpj_ent = entrada(self.frame_ent)
        self.cnpj_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.telefone_ent = entrada(self.frame_ent)
        self.telefone_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.endereco_ent = entrada(self.frame_ent)
        self.endereco_ent.et.pack(side=TOP, anchor='w',pady=6)
        
    # -------- Botao de cadastrar ------------
        
        self.botao_cadastrar = Button(self.janela)
        self.botao_cadastrar.configure(
            text='Cadastrar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold'),
            command=self.cadastrar
        )
        self.botao_cadastrar.place(relx=0.40,rely=0.90)
        
    def cadastrar(self):
        txt = ''
        self.Nome = self.nome_ent.et.get()
        if self.Nome == '':
            txt += 'Insira o Nome da Cl??nica!\n'

        self.CNPJ = self.cnpj_ent.et.get()
        if self.CNPJ == '':
            txt += 'Insira o CNPJ da Cl??nica!\n'
            
        self.Telefone = self.telefone_ent.et.get()
        if self.Telefone == '':
            txt += 'Insira o Telefone da Cl??nica!\n'
            
        self.Endereco = self.endereco_ent.et.get()
        if self.Endereco == '':
            txt += 'Insira do Endere??o da Cl??nica!\n'
        #self.Servicos = [self.var_tosa.get(),self.var_castracao.get(),self.var_internacao.get()]
        
        if txt == '':
            #try:
            BD.Registrar_Clinica(self.Nome,self.CNPJ,self.Telefone,self.Endereco)
            messagebox.showinfo(title="Cadastro Info",message="Cadastrado com Sucesso!!\n")
            self.root.destroy()
            #except:
                #messagebox.showinfo(title="Cadastro Info",message="Houve Algum Problema!\n")
        else:
            messagebox.showinfo(title="Cadastro Info",message=txt)
            
window = Tk()  
cadastro = CadCli(window)
window.mainloop()