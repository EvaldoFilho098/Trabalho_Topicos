from tkinter import filedialog as dlg, messagebox
from tkinter import *
import banco_de_dados as BD
from TabelaAdotantes import VisualizarPessoas
from TabelaPets import VisualizarPets


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
        )
        self.frame_lbs.place(relx=0.05, rely=0.2,relwidth=0.45,relheight=0.95)
        
        self.frame_ent = Frame(self.janela)
        self.frame_ent.configure(
            bg="#086788",
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
            font=('Verdana', 8, 'bold'),
            command=self.cadastrar_adocao
        )
        self.botao_cadastrar.place(relx=0.435,rely=0.90)
    
        self.ID_Pet_Selecionado = ''
        self.ID_Adotante_Selecionado = ''
    
    def cadastrar_adocao(self):
        txt = ''
        
        if self.ID_Adotante_Selecionado == '':
            txt += 'Selecione um Adotante!\n'
            
        if self.ID_Pet_Selecionado == '':
            txt += 'Selecione um Pet!\n'
        
        self.Data = self.data_visita_ent.et.get()
        if self.Data == '':
            txt += 'Insira uma Data para Visita!\n'
        
        if txt == '':
            try:
                BD.Registrar_Adocao(self.Data,'Em Analise',self.ID_Pet_Selecionado[0],self.ID_Adotante_Selecionado[0])
                BD.alterar_status_pet(self.ID_Pet_Selecionado[0],'Análise')
                messagebox.showinfo(title="Cadastro Info",message="Cadastrado com Sucesso!!\n")
                self.root.destroy()
            except:
                messagebox.showinfo(title="Cadastro Info",message="Houve Algum Problema!\n")
        else:
            messagebox.showinfo(title="Cadastro Info",message=txt)
            
    # ------------------ Selecionando Adotante ---------------------- #
    def selecionar_adotante(self):
        self.visualizar_adotantes = VisualizarPessoas(self.root)
        self.visualizar_adotantes.bt_Selecionar.Botao.config(command=self.botao_selecionar_adotante)
    
    def botao_selecionar_adotante(self):
        try:
            node_pessoa = self.visualizar_adotantes.Tabela_Pessoas.Listagem.focus()
            self.ID_Adotante_Selecionado = (self.visualizar_adotantes.Tabela_Pessoas.Listagem.item(node_pessoa)['values'][0],self.visualizar_adotantes.Tabela_Pessoas.Listagem.item(node_pessoa)['values'][1])
            self.visualizar_adotantes.root.destroy()
            self.lbl_Adotante_Selecionado = Label(self.frame_ent,text=self.ID_Adotante_Selecionado[1],font=('verdana',8,'bold underline'),bg='#086788',fg='white')
            self.lbl_Adotante_Selecionado.place(relx=0.32,rely= 0.051)
            #print(self.ID_Adotante_Selecionado)
        except:
            messagebox.showinfo(title='Erro',message='Selecione um Adotante\n')
    
     # ------------------ Selecionando PET ---------------------- #
    def selecionar_pet(self):
        self.visualizar_pets = VisualizarPets(self.root,'selecionar','disponiveis')
        self.visualizar_pets.bt_Selecionar.Botao.config(command=self.botao_selecionar_pet)
    
    def botao_selecionar_pet(self):
        try:
            node_pet = self.visualizar_pets.Tabela_Pets.Listagem.focus()
            self.ID_Pet_Selecionado = (self.visualizar_pets.Tabela_Pets.Listagem.item(node_pet)['values'][0],self.visualizar_pets.Tabela_Pets.Listagem.item(node_pet)['values'][1],self.visualizar_pets.Tabela_Pets.Listagem.item(node_pet)['values'][5])
            if self.ID_Pet_Selecionado[2] == 'Não Liberado':
                messagebox.showinfo(title='Erro',message='Pet Não Liberado para Adoção!\n')
            else:
                self.visualizar_pets.root.destroy()
                self.lbl_Pet_Selecionado = Label(self.frame_ent,text=self.ID_Pet_Selecionado[1],font=('verdana',8,'bold underline'),bg='#086788',fg='white')
                self.lbl_Pet_Selecionado.place(relx=0.32,rely= 0.24)
                #print(self.ID_Pet_Selecionado)
        except:
            messagebox.showinfo(title='Erro',message='Selecione um Pet!\n')
    
    # ------------------ Formatando entrarda da Data ---------------------- #
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
        
    
    
#window = Tk()
#cadastro = Adocao(window)
#window.mainloop()