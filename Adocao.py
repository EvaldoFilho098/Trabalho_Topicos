from tkinter import filedialog as dlg
from tkinter import *

from TabelaAdotantes import VisualizarPessoas
from TabelaPets import VisualizarPets

#window = Tk()

# -----------------------Class Entry----------------------- #
class entrada:
    def __init__(self, container):
        self.et = Entry(container)
        self.et.configure(
            bg='#C4C4C4',
            fg='black',
            width=15,
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

# -----------------------Tela----------------------- #

class Adocao:
    def __init__(self, master):
        self.root = Toplevel(master)
        #self.root = master 
        self.tela()
        self.adicionar_elementos()
        self.root.grab_set()
    
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
            #bd=4,
            #highlightbackground="grey",
            #highlightthickness='3px'
        )
        self.frame_lbs.place(relx=0.05, rely=0.2,relwidth=0.45,relheight=0.95)
        
        self.frame_ent = Frame(self.janela)
        self.frame_ent.configure(
            bg="#086788",
            #bd=4,
            #highlightbackground="grey",
            #highlightthickness='3px'
        )
        self.frame_ent.place(relx=0.50, rely=0.2,relwidth=0.45,relheight=0.95)

    #---- titulo tela ----#
    
        self.nome_empresa = Label(self.janela)
        self.nome_empresa.configure(
            text="ADOÇÃO",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 24, 'bold')
        )
        self.nome_empresa.place(relx=0.35, rely=0.02)
    
    #---- Criando Label's da tela ----#
        self.nome_box = textos(self.frame_lbs)
        self.nome_box.lb.configure(text='Adotante:')
        self.nome_box.lb.pack(side=TOP, anchor='e',pady=10)

        self.sel_pet_box = textos(self.frame_lbs)
        self.sel_pet_box.lb.configure(text='Pet:')
        self.sel_pet_box.lb.pack(side=TOP, anchor='e',pady=10)
        
        self.data_visita_box = textos(self.frame_lbs)
        self.data_visita_box.lb.configure(text='Data de Visita:')
        self.data_visita_box.lb.pack(side=TOP, anchor='e',pady=10)

        
    #---- Criando Entry's da tela ----#
        self.sel_adotante_bt = Button(self.frame_ent)
        self.sel_adotante_bt.configure(
            text='Selecionar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold'),
            command=self.selecionar_adotante
        )
        self.sel_adotante_bt.pack(side=TOP, anchor='w',pady=14)

        self.sel_pet_bt = Button(self.frame_ent)
        self.sel_pet_bt.configure(
            text='Selecionar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold'),
            command=self.selecionar_pet
        )
        self.sel_pet_bt.pack(side=TOP, anchor='w',pady=14)
        
        self.data_visita_ent = entrada(self.frame_ent)
        self.data_visita_ent.et.pack(side=TOP, anchor='w',pady=14)
        self.data_visita_ent.et.bind("<KeyRelease>", self.format_data)
        
    # -------- Botao de cadastrar ------------
        
        self.botao_cadastrar = Button(self.janela)
        self.botao_cadastrar.configure(
            text='Cadastrar',
            bg='#C4C4C4',
            font=('Verdana', 8, 'bold')
        )
        self.botao_cadastrar.place(relx=0.40,rely=0.90)
    
    def selecionar_pet(self):
        VisualizarPets(self.root)
        
    def selecionar_adotante(self):
        VisualizarPessoas(self.root)
        
    def format_data(self,event = None):
    
        text = self.data_visita_ent.et.get().replace("/", "")[:8]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue

            if index == 1: new_text +=  text[index] + "/" 
            elif index == 3: new_text += text[index] + "/"
            else: new_text += text[index]

        self.data_visita_ent.et.delete(0, "end")
        self.data_visita_ent.et.insert(0, new_text)
    

        
        
#cadastro = Adocao(window)

#window.mainloop()