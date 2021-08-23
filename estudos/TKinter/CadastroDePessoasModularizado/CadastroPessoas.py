from tkinter import tix

from Modulos import *
from Funcoes import *
from Relatorios import *
from GradientFrame import *
from Validadores import *


class Aplicacao(Funcoes, Relatorios, Validadores):
    def __init__(self):
        self.root = tix.Tk()
        self.imagens_base64()
        self.tela()
        self.validaEntradas()
        self.frames()
        self.botoes()
        self.labelsEentrys()
        self.lista()
        self.montaTabelas()
        self.select_lista()
        self.menus()
        self.root.mainloop()

    def tela(self):
        self.root.title('Cadastro de clientes')  # Cria um texto na barra superior da janela
        self.root.configure(background='#1e3743')  # Muda a cor de fundo
        self.root.geometry('700x500')  # Tamanho inicial da janela HorizontalxVertical
        self.root.resizable(True, True)  # Permite ou não o ajuste da tela ( aumentar ou diminuir )
        self.root.maxsize(width=900, height=700)  # tamanho maximo da tela
        self.root.minsize(width=600, height=400)  # tamanho minimo

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg='AliceBlue',
                            highlightbackground='#4B0082', highlightthickness=2)
        # Criando o frame1, com borda 4, background = Alice blue, cor da borda = , largura da borda = 2
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # tamanho do frame em porcentagem HorizontalxVertical

        self.frame2 = Frame(self.root, bg='AliceBlue', bd=4,
                            highlightbackground='#4B0082', highlightthickness=2)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        abas = ttk.Notebook(self.frame1)
        self.aba1 = GradientFrame(abas)
        self.aba2 = GradientFrame(abas)

        self.aba1.configure(background='aliceBlue')

        self.aba2.configure(background='AliceBlue')

        abas.add(self.aba1, text='Aba 1')
        abas.add(self.aba2, text='Aba 2')

        abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

    def botoes(self):
        # moldura
        canvas1_bt = Canvas(self.aba1, bd=0, bg='#1E3743', highlightbackground='gray', highlightthickness=3)
        canvas1_bt.place(relx=0.195, rely=0.085, relwidth=0.23, relheight=0.18)

        canvas2_bt = Canvas(self.aba1, bd=0, bg='#1E3743', highlightbackground='gray', highlightthickness=3)
        canvas2_bt.place(relx=0.595, rely=0.085, relwidth=0.35, relheight=0.18)

        # LIMPAR
        bt_limpar = Button(self.aba1, text='Limpar', bd=4, bg='#107db2', fg='#FFFFF0',
                           activebackground='#107db2', activeforeground='white',
                           font=('Arial', 9, 'bold'), command=self.limpaTela)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # BUSCAR
        bt_buscar = Button(self.aba1, text='Buscar', bd=4, bg='#107db2', fg='#FFFFF0',
                           activebackground='#107db2', activeforeground='white',
                           font=('Arial', 9, 'bold'), command=self.buscar)
        bt_buscar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.15)

        #  Balão de mensagem botão buscar
        balao_buscar = tix.Balloon(self.aba1)
        txt_buscar = 'Digite o nome do cliente que deseja buscar no sistema'
        balao_buscar.bind_widget(bt_buscar, balloonmsg=txt_buscar)

        #  IMAGEM BOTÃO NOVO
        """btnovo = PhotoImage(file=base64.b64decode(self.btnovo_base64))
        imgNovo = btnovo.subsample(2, 2)

        style = ttk.Style()
        style.configure("BW.TButton", relwidth=1, relheight=1, foreground='gray', borderwidth=0,
                        bordercolor='gray', background='#dfe3ee', image=imgNovo)"""

        # NOVO
        bt_novo = Button(self.aba1, text='Novo', bd=4, bg='#107db2', fg='#FFFFF0',
                         activebackground='#107db2', activeforeground='white',
                         font=('Arial', 9, 'bold'), command=self.add_cliente)
        bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        "bt_novo.config(image=imgNovo)"

        # ALTERAR
        bt_alterar = Button(self.aba1, text='Alterar', bd=4, bg='#107db2', fg='#FFFFF0',
                            activebackground='#107db2', activeforeground='white',
                            font=('Arial', 9, 'bold'), command=self.altera_cliente)
        bt_alterar.place(relx=0.72, rely=0.1, relwidth=0.1, relheight=0.15)

        # APAGAR
        bt_apagar = Button(self.aba1, text='Apagar', bd=4, bg='#107db2', fg='#FFFFF0',
                           activebackground='#107db2', activeforeground='white',
                           font=('Arial', 9, 'bold'), command=self.deleta_cliete)
        bt_apagar.place(relx=0.84, rely=0.1, relwidth=0.1, relheight=0.15)

        # Drop down button
        tipvar = StringVar()
        tipv = ("Solteiro(a)", "Namorando(a)", "Casado(a)", "Viuvo(a)")
        tipvar.set("Solteiro")
        popupMenu = OptionMenu(self.aba2, tipvar, *tipv)
        popupMenu.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.15)
        #  estado_civil = tipvar.get()
        #  print(estado_civil)

    def labelsEentrys(self):
        # CÓDIGO
        lb_code = Label(self.aba1, text='Código', bg='AliceBlue', fg='#0000CD', font=('Arial', 9, 'bold'))
        lb_code.place(relx=0.03, rely=0.06, relwidth=0.08, relheight=0.08)
        self.et_code = Entry(self.aba1, bg='#FFFAFA', fg='#363636', validate='key', validatecommand=self.vcmd2)
        self.et_code.place(relx=0.02, rely=0.15, relwidth=0.15, relheight=0.1)

        # NOME
        lb_nome = Label(self.aba1, text='Nome', bg='AliceBlue', fg='#0000CD', font=('Arial', 9, 'bold'))
        lb_nome.place(relx=0.03, rely=0.41, relwidth=0.08, relheight=0.08)
        self.et_nome = Entry(self.aba1, bg='#FFFAFA', fg='#363636')
        self.et_nome.place(relx=0.02, rely=0.5, relwidth=0.93, relheight=0.13)

        # TELEFONE
        lb_telefone = Label(self.aba1, text='Telefone', bg='AliceBlue', fg='#0000CD', font=('Arial', 9, 'bold'))
        lb_telefone.place(relx=0.03, rely=0.71, relwidth=0.09, relheight=0.08)
        self.et_telefone = Entry(self.aba1, bg='#FFFAFA', fg='#363636')
        self.et_telefone.place(relx=0.02, rely=0.8, relwidth=0.3, relheight=0.12)

        # CIDADE
        lb_cidade = Label(self.aba1, text='Cidade', bg='AliceBlue', fg='#0000CD', font=('Arial', 9, 'bold'))
        lb_cidade.place(relx=0.41, rely=0.71, relwidth=0.08, relheight=0.08)
        self.et_cidade = Entry(self.aba1, bg='#FFFAFA', fg='#363636')
        self.et_cidade.place(relx=0.4, rely=0.8, relwidth=0.55, relheight=0.12)

        # CALENDARIO
        bt_calendario = Button(self.aba2, text='Data', command=self.calendario)
        bt_calendario.place(relx=0.5, rely=0.05, relwidth=0.1, relheight=0.13)
        self.data_et = Entry(self.aba2, width=10)
        self.data_et.place(relx=0.5, rely=0.2)

    def lista(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.05, rely=0.05, relwidth=0.85, relheight=0.9)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)  # barra de rolagem pertence a listaCli
        self.scrollLista.place(relx=0.9, rely=0.05, relwidth=0.05, relheight=0.9)

        self.listaCli.bind('<Double-1>', self.OnDoubleClick)

    def menus(self):
        menubar = Menu(self.root)
        self.root.configure(menu=menubar)
        fileMenu1 = Menu(menubar)
        fileMenu2 = Menu(menubar)

        def sair(): self.root.destroy()

        menubar.add_cascade(label="opções", menu=fileMenu1)
        menubar.add_cascade(label="Relatórios", menu=fileMenu2)

        fileMenu1.add_command(label='Sair', command=sair)
        fileMenu1.add_command(label='Limpa Cliente', command=self.limpaTela)
        fileMenu2.add_command(label='Ficha do cliente', command=self.GeraRelatorio)

    def janela2(self):
        root2 = Toplevel()
        root2.title("Janela 2")
        root2.configure(bg='AliceBlue')
        root2.geometry("400x200")
        root2.resizable(False, False)
        root2.transient(self.root)
        root2.focus_force()
        root2.grab_set()

    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2), "%P")


app = Aplicacao()
