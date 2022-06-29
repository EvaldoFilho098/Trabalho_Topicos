from tkinter import filedialog as dlg
from tkinter import *

#window = Tk()

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
        self.root = Toplevel(master)
        #self.root = master
        self.tela()
        self.adicionar_elementos()
        self.root.mainloop()
    
    def tela(self):
        self.root.title("Love Pet")
        self.root.geometry("600x500")
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
            #bd=4,
            #highlightbackground="grey",
            #highlightthickness='3px'
        )
        self.frame_lbs.place(relx=0.05, rely=0.2,relwidth=0.35,relheight=0.95)
        
        self.frame_ent = Frame(self.janela)
        self.frame_ent.configure(
            bg="#086788",
            #bd=4,
            #highlightbackground="grey",
            #highlightthickness='3px'
        )
        self.frame_ent.place(relx=0.40, rely=0.2,relwidth=0.45,relheight=0.95)

    #---- titulo tela ----#
    
        self.nome_empresa = Label(self.janela)
        self.nome_empresa.configure(
            text="CADASTRAR CLÍNICA",
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
        self.endereco_box.lb.configure(text='Endereço:')
        self.endereco_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.espaco_2box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_2box.lb.pack(side=TOP, anchor='e')

        self.tipo_box = textos(self.frame_lbs)
        self.tipo_box.lb.configure(text='Serviços:')
        self.tipo_box.lb.pack(side=TOP, anchor='e',pady=5)
        

        
    #---- Criando Entry's da tela ----#
        self.nome_ent = entrada(self.frame_ent)
        self.nome_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.cnpj_ent = entrada(self.frame_ent)
        self.cnpj_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.telefone_ent = entrada(self.frame_ent)
        self.telefone_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.endereco_ent = entrada(self.frame_ent)
        self.endereco_ent.et.pack(side=TOP, anchor='w',pady=6)
     
        self.espaco_2ent = textos(self.frame_ent) # -------------------- Espaco
        self.espaco_2ent.lb.pack(side=TOP, anchor='w',pady=2)
        
        self.var_tosa = BooleanVar()
        self.servico_tosa = opcoes(self.frame_ent,self.var_tosa,'Tosa')
        self.servico_tosa.op.pack(side=TOP, anchor='w')
        
        self.var_castracao = BooleanVar()
        self.servico_castracao = opcoes(self.frame_ent,self.var_castracao,'Castração')
        self.servico_castracao.op.pack(side=TOP, anchor='w')
        
        self.var_internacao = BooleanVar()
        self.servico_internacao = opcoes(self.frame_ent,self.var_internacao,'Internação')
        self.servico_internacao.op.pack(side=TOP, anchor='w')
        
    # -------- Botao de cadastrar ------------
        
        self.botao_cadastrar = Button(self.janela)
        self.botao_cadastrar.configure(
            text='Cadastrar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold')
        )
        self.botao_cadastrar.place(relx=0.40,rely=0.90)
        
        
        
#cadastro = CadCli(window)

#window.mainloop()