from tkinter import *

window = Tk()
window.title("Love Pet")
window.geometry("1024x600")
window.configure(bg="#086788")
#window.resizable(False, False)
#teste
# -----------------------Class Entry----------------------- #


class entrada:
    def __init__(self, container):
        self.et = Entry(container)
        self.et.configure(
            bg='#C4C4C4',
            fg='black',
            width=30,
            font=('Verdana', 15)
        )

# -----------------------Class Label----------------------- #


class textos:
    def __init__(self, container):
        self.lb = Label(container)
        self.lb.configure(
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 20, 'bold')
        )

# -----------------------Class Canvas----------------------- #


class Mypage(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        self.canvas = Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scroll_bar = Scrollbar(
            self, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.scroll_bar.set)

        self.internal_frame = Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.internal_frame, anchor='nw')

        self.__build()
        self.internal_frame.update_idletasks()

        self.config(width=2048, height=1200)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def __build(self):
        #---- criando a Janela ----#
        janela = Frame(self.internal_frame)
        janela.configure(
            bg="#086788",
            width=2048,
            height=1200,
            highlightbackground="#086788",
            highlightthickness='0px'
        )
        janela.pack(anchor='center')

    #---- titulo tela ----#

        nome_empresa = Label(janela)
        nome_empresa.configure(
            text="CADASTRO",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 40, 'bold')
        )
        nome_empresa.place(x=338, y=1)

    #---- Criando Label's da tela ----#
        nome_box = textos(janela)
        nome_box.lb.configure(text='Nome:')
        nome_box.lb.place(x=260, y=104)

        cpf_box = textos(janela)
        cpf_box.lb.configure(text='CPF:')
        cpf_box.lb.place(x=291, y=146)

        email_box = textos(janela)
        email_box.lb.configure(text='E-mail:')
        email_box.lb.place(x=253, y=184)

        tel_box = textos(janela)
        tel_box.lb.configure(text='Telefone:')
        tel_box.lb.place(x=220, y=224)

        senh_box = textos(janela)
        senh_box.lb.configure(text='Crie uma senha:')
        senh_box.lb.place(x=116, y=284)

        senConf_box = textos(janela)
        senConf_box.lb.configure(text='Confirme a senha:')
        senConf_box.lb.place(x=86, y=324)

    #---- Criando Entry's da tela ----#
        nome_ent = entrada(janela)
        nome_ent.et.place(x=370, y=112)

        cpf_ent = entrada(janela)
        cpf_ent.et.place(x=370, y=152)

        email_ent = entrada(janela)
        email_ent.et.place(x=370, y=192)

        tel_ent = entrada(janela)
        tel_ent.et.place(x=370, y=232)

        sen_ent = entrada(janela)
        sen_ent.et.place(x=370, y=292)

        senConf_ent = entrada(janela)
        senConf_ent.et.place(x=370, y=332)


cadastro = Mypage(window)

window.mainloop()
