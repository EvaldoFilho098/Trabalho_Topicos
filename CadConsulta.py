from msilib.schema import ComboBox
from tkinter import filedialog as dlg, messagebox
from tkinter import *
from tkinter.ttk import Combobox

import banco_de_dados as BD

#window = Tk()


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

class CadConsulta:
    def __init__(self, master, id_pet):
        
        self.root = Toplevel(master)
        #self.root = master
        self.master = master
        self.id_pet = id_pet
        self.tela()
        self.adicionar_elementos()
        self.root.grab_set()
    
    def tela(self):
        self.root.title("Love Pet")
        self.root.geometry("500x300")
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
            text="NOVA CONSULTA",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 24, 'bold')
        )
        self.nome_empresa.place(relx=0.18, rely=0.02)
    
    #---- Criando Label's da tela ----#
        self.clinica_box = textos(self.frame_lbs)
        self.clinica_box.lb.configure(text='Clínica:')
        self.clinica_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.servicos_box = textos(self.frame_lbs)
        self.servicos_box.lb.configure(text='Serviços:')
        self.servicos_box.lb.pack(side=TOP, anchor='e',pady=2)

        self.espaco_2box = textos(self.frame_lbs) # -------------------- Espaco
        self.espaco_2box.lb.pack(side=TOP, anchor='e',pady=18)

        self.valor_box = textos(self.frame_lbs)
        self.valor_box.lb.configure(text='Valor:')
        self.valor_box.lb.pack(side=TOP, anchor='e',pady=2)
 
        
    #---- Criando Entry's da tela ----#

        self.clinica_selecionada = StringVar()
        self.clinica_ent = Combobox(self.frame_ent, textvariable=self.clinica_selecionada)
        self.Clinicas_ID = BD.busca_clinicas()
        self.Clinicas = []
        for item in self.Clinicas_ID:
            self.Clinicas.append(item[0])
        self.clinica_ent['values'] = self.Clinicas
        self.clinica_ent['state'] = 'readonly'
        self.clinica_ent.pack(side=TOP, anchor='w',pady=6,padx=2)

        self.servicos_ent = Text(self.frame_ent)
        self.servicos_ent.config(width=20,height=5)
        self.servicos_ent.pack(side=TOP, anchor='w',pady=10,padx=2)

        self.valor_ent = Entry(self.frame_ent)
        self.valor_ent.configure(
            bg='white',#C4C4C4
            fg='black',
            width=10,
            font=('Verdana', 12)
        )
        self.valor_ent.insert(0,'R$')
        self.valor_ent.pack(side=TOP, anchor='w',pady=6,padx=2)

        
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

        self.Clinica = self.clinica_selecionada.get()
        for item in range(len(self.Clinicas_ID)):
            if self.Clinica in self.Clinicas_ID[item]:
                self.Clinica = self.Clinicas_ID[item][1]
                break
        if self.Clinica == '':
            txt += 'Selecione a Clinica\n'

        self.Servicos = self.servicos_ent.get("1.0", "end-1c")
        if self.Servicos == '':
            txt += 'Descreva os Serviços\n'

        self.Valor = self.valor_ent.get()
        if 'R$' not in self.Valor: 
            self.Valor = 'R$' + self.Valor
        if ',' not in self.Valor:
            self.Valor += ',00'
        if self.Valor == 'R$,00':
            txt += 'Insira o Valor da Consulta\n'
        
        if txt == '':
            try:
                BD.Registrar_Atendimento(self.Servicos,self.Valor,self.Clinica,self.id_pet)
                messagebox.showinfo(title="Cadastro Info",message="Cadastrado com Sucesso!!\n")
                self.root.destroy()
            except:
                messagebox.showinfo(title="Cadastro Info",message="Houve Algum Problema!\n")
        else: 
            messagebox.showinfo(title="Cadastro Info",message=txt)

#window = Tk() 
#cadastro = CadConsulta(window,1)
#window.mainloop()