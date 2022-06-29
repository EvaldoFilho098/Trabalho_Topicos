from tkinter import HORIZONTAL, VERTICAL, ttk
from tkinter import *

class Tabelas:
    def __init__(self,master,colunas,qtd_linhas=15,largura=100,lar_min=100,estilo=''):
        
        self.Colunas = colunas
        self.Largura = largura
        self.Altura = qtd_linhas
        if estilo == '':
            self.Listagem = ttk.Treeview(master,columns = self.Colunas,show='headings', height = qtd_linhas, selectmode='browse')
        else:
            self.Listagem = ttk.Treeview(master,columns = self.Colunas,show='headings', height = qtd_linhas, selectmode='browse',style=estilo)
        
        for new in self.Colunas:
            if new == 'ID':
                self.Listagem.column(str(new), width = 15, minwidth=15, anchor='center')
            else:
                self.Listagem.column(str(new), width = largura, minwidth=lar_min,anchor='center')
            
            self.Listagem.heading(str(new),text=str(new))

        #BARRAS DE ROLAGEM DA VISUALIZACAO
        self.Barra_Y= ttk.Scrollbar(master, orient=VERTICAL,command=self.Listagem.yview)

        self.Barra_X = ttk.Scrollbar(master, orient=HORIZONTAL,command=self.Listagem.xview)

        self.Listagem.configure(yscroll = self.Barra_Y.set)
        self.Listagem.configure(xscroll = self.Barra_X.set)

        # TEXTOS DOS CABEÇALHO
        for c in self.Colunas:
            self.Listagem.heading(str(c), text=str(c))
        
        self.Infos = []

    def Inserir(self,lista):
        # INSRINDO OS ITENS
        """
        lista precisa ser uma lista de tuplas
        """
        try:
            for i in lista:
                item = tuple(i)
                self.Listagem.insert('','end', values=item)
        except:
            pass
    
    