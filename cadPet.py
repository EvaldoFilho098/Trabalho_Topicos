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

class CadPet:
    def __init__(self, master):
        self.root = Toplevel(master)
        self.tela()
        self.adicionar_elementos()
        self.root.grab_set()
    
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
            text="CADASTRAR PET",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 24, 'bold')
        )
        self.nome_empresa.place(relx=0.25, rely=0.02)
    
    #---- Criando Label's da tela ----#
        self.nome_box = textos(self.frame_lbs)
        self.nome_box.lb.configure(text='Nome:')
        self.nome_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.raca_box = textos(self.frame_lbs)
        self.raca_box.lb.configure(text='Raça:')
        self.raca_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.genero_box = textos(self.frame_lbs)
        self.genero_box.lb.configure(text='Gênero:')
        self.genero_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.idade_box = textos(self.frame_lbs)
        self.idade_box.lb.configure(text='Idade:')
        self.idade_box.lb.pack(side=TOP, anchor='e',pady=2)
        
        self.espaco_2box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_2box.lb.pack(side=TOP, anchor='e')

        self.tipo_box = textos(self.frame_lbs)
        self.tipo_box.lb.configure(text='Status:')
        self.tipo_box.lb.pack(side=TOP, anchor='e',pady=3)
        
        self.espaco_3box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_3box.lb.pack(side=TOP, anchor='e',pady=26)
        
        self.senh_box = textos(self.frame_lbs)
        self.senh_box.lb.configure(text='Imagem:')
        self.senh_box.lb.pack(side=TOP, anchor='e',pady=2)

        
    #---- Criando Entry's da tela ----#
        self.nome_ent = entrada(self.frame_ent)
        self.nome_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.raca_ent = entrada(self.frame_ent)
        self.raca_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.genero_ent = entrada(self.frame_ent)
        self.genero_ent.et.pack(side=TOP, anchor='w',pady=6)

        self.idade_ent = entrada(self.frame_ent)
        self.idade_ent.et.pack(side=TOP, anchor='w',pady=6)
     
        self.espaco_2ent = textos(self.frame_ent) # -------------------- Espaco
        self.espaco_2ent.lb.pack(side=TOP, anchor='w',pady=2)
        
        self.var = StringVar()
        self.tipo_liberado = opcoes(self.frame_ent,self.var,'Liberado','Liberado Para Adoção')
        self.tipo_liberado.op.pack(side=TOP, anchor='w')
        
        self.tipo_nao_liberado = opcoes(self.frame_ent,self.var,'Nao_Liberado','Não Liberado Para Adoção')
        self.tipo_nao_liberado.op.pack(side=TOP, anchor='w')
        
        
        self.espaco_3ent = textos(self.frame_ent) # -------------------- Espaco
        self.espaco_3ent.lb.pack(side=TOP, anchor='w',pady=16)

        self.sel_img_bt = Button(self.frame_ent)
        self.sel_img_bt.config(
            text='Selecionar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold'),
            command=self.selecionar_imagem,
            )
        self.sel_img_bt.pack(side=TOP, anchor='w')

    # -------- Botao de cadastrar ------------
        
        self.botao_cadastrar = Button(self.janela)
        self.botao_cadastrar.configure(
            text='Cadastrar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold'),
            command=self.cadastrar
        )
        self.botao_cadastrar.place(relx=0.40,rely=0.90)
        
        self.diretorio_img_lb = Label(self.frame_ent)
        self.diretorio_img_lb.config(
            bg = '#086788',
            fg = 'white',
            font = ('verdana',7,'bold underline')
        )
        
    def selecionar_imagem(self):
        self.diretorio_img = dlg.askopenfilename()
        self.diretorio_img_lb.config(text = self.diretorio_img.split('/')[-1])
        self.diretorio_img_lb.pack(side=TOP,anchor='w')
        
    def cadastrar(self):
        txt = ''
        self.Nome = self.nome_ent.et.get()
        if self.Nome == '':
            txt += 'Inserir o Nome do Pet!\n'
            
        self.Raca = self.raca_ent.et.get()
        if self.Raca == '':
            txt += 'Inserir a Raça do Pet!\n'
            
        self.Genero = self.genero_ent.et.get()
        if self.Genero == '':
            txt += 'Inserir o Gênero do Pet!\n'
            
        self.Idade = self.idade_ent.et.get()
        if self.Idade == '':
            txt += 'Inserir a Idade do Pet!\n'
            
        self.Status = self.var.get()
        if self.Status == '':
                txt += 'Selecione o Status do Pet!\n'
        
        try:
            self.Foto_dir = self.diretorio_img
            if self.Foto_dir == '':
                txt += 'Escolher foto do Pet!\n'
        except:
            txt += 'Escolher foto do Pet!\n'
            
        if txt == '':
            try:
                BD.Registrar_Pet(self.Nome,self.Raca,self.Genero,self.Idade,self.Status,self.Foto_dir)
                messagebox.showinfo(title="Cadastro Info",message="Cadastrado com Sucesso!!\n")
                self.root.destroy()
            except:
                messagebox.showinfo(title="Cadastro Info",message="Houve Algum Problema!\n")
        else:
            messagebox.showinfo(title="Cadastro Info",message=txt)
            
#window = Tk()
#cadastro = CadPet(window)
#window.mainloop()