from imports import *
from Validadores import Validadores
from Funcs import Funcs


class Interface(Validadores, Funcs):
    def __init__(self):
        self.raiz = tix.Tk()

        #  variaveis
        self.frame1 = Frame(self.raiz, bg='AliceBlue', highlightbackground='gray', highlightthickness=3)

        self.ValidaEntradas()
        self.telaPrimaria()
        self.abas()
        self.adicionar_veiculo()
        self.alterar_veiculo()
        self.apagar_veiculo()
        self.lista_veiculos()
        self.tabelaCarros()
        self.tabelaPrecos()
        self.menu()
        self.dados()
        self.raiz.mainloop()

    def telaPrimaria(self):
        self.raiz.geometry('1000x500')
        self.raiz.title('Anthony Parks')
        self.raiz.minsize(800, 400)
        self.raiz.configure(bg='#1E90FF')
        titulo = Label(self.raiz, text='Anthony Park', font=('Comic Sans MS', 18), bg='#1E90FF')
        titulo.place(relx=0.4, rely=0.01, relwidth=0.2, relheight=0.06)

    def abas(self):
        abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(abas)
        self.aba2 = Frame(abas)
        self.aba3 = Frame(abas)

        self.aba1.configure(background='AliceBlue')
        self.aba2.configure(background='AliceBlue')
        self.aba3.configure(background='AliceBlue')

        abas.add(self.aba1, text='Adicionar cliente')
        abas.add(self.aba3, text='Alterar cliente')
        abas.add(self.aba2, text='Pagamento')
        abas.place(relx=0, rely=0, relwidth=1, relheight=1)

    def adicionar_veiculo(self):  # novo carro
        self.frame1.place(relx=0.025, rely=0.08, relwidth=0.95, relheight=0.43)

        #  PLACA
        placa_lb = Label(self.aba1, text='Placa:', bg='AliceBlue', anchor='w')
        placa_lb.place(relx=0.03, rely=0.2, relwidth=0.1, relheight=0.17)
        self.placa_et = Entry(self.aba1, highlightbackground='gray', highlightthickness=2, validate='key',
                              validatecommand=self.valPlaca)
        self.placa_et.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.17)

        #  MODELO
        modelo_lb = Label(self.aba1, text='Modelo:', bg='AliceBlue', anchor='w')
        modelo_lb.place(relx=0.03, rely=0.7, relwidth=0.1, relheight=0.15)
        self.modelo_et = Entry(self.aba1, highlightbackground='gray', highlightthickness=2, validate='key',
                               validatecommand=self.valModel)
        self.modelo_et.place(relx=0.1, rely=0.7, relwidth=0.5, relheight=0.17)
        opcional = Label(self.aba1, text='( Opcional )', bg='AliceBlue', anchor='w')
        opcional.place(relx=0.61, rely=0.7, relwidth=0.08, relheight=0.15)

        #  ADICIONAR
        add_canvas = Canvas(self.aba1, bg='AliceBlue', bd=4, highlightbackground='gray', highlightthickness=3)
        add_canvas.place(relx=0.698, rely=0.39, relwidth=0.254, relheight=0.24)

        adicionar_bt = Button(self.aba1, text='Adicionar', bg='#87CEEB', activebackground='#87CEEB',
                              activeforeground='black', command=self.adicionar)
        adicionar_bt.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.22)

        add_balao = tix.Balloon(self.aba1)
        add_txt = 'Ao clicar, adiciona um veiculo no sistema com as informações fornecidas nos campos acima'
        add_balao.bind_widget(adicionar_bt, balloonmsg=add_txt)

    def alterar_veiculo(self):
        Canvas(self.aba3, bg='AliceBlue', highlightbackground='gray', highlightthickness=3).place(relx=0.027, rely=0.22, relwidth=0.256, relheight=0.178)
        id_lb = Label(self.aba3, text='Código:', bg='AliceBlue')
        id_lb.place(relx=0.03, rely=0.05, relwidth=0.25, relheight=0.15)
        self.idAlt_et = Entry(self.aba3, validate='key', validatecommand=self.valcod)
        self.idAlt_et.place(relx=0.03, rely=0.23, relwidth=0.25, relheight=0.15)

        Canvas(self.aba3, bg='AliceBlue', highlightbackground='gray', highlightthickness=3).place(relx=0.027, rely=0.69, relwidth=0.256, relheight=0.178)
        modelo_lb = Label(self.aba3, text='Modelo:', bg='AliceBlue')
        modelo_lb.place(relx=0.03, rely=0.57, relwidth=0.25, relheight=0.08)
        self.modeloAlt_et = Entry(self.aba3)
        self.modeloAlt_et.place(relx=0.03, rely=0.7, relwidth=0.25, relheight=0.15)

        Canvas(self.aba3, bg='AliceBlue', highlightbackground='gray', highlightthickness=3).place(relx=0.328, rely=0.43, relwidth=0.256, relheight=0.188)
        placa_lb = Label(self.aba3, text='Placa:', bg='AliceBlue')
        placa_lb.place(relx=0.33, rely=0.34, relwidth=0.25, relheight=0.08)
        self.placaAlt_et = Entry(self.aba3, validate='key', validatecommand=self.valPlaca)
        self.placaAlt_et.place(relx=0.33, rely=0.44, relwidth=0.25, relheight=0.16)

        Canvas(self.aba3, bg='AliceBlue', highlightbackground='gray', highlightthickness=3).place(relx=0.697, rely=0.39, relwidth=0.256, relheight=0.22)
        alterar_bt = Button(self.aba3, text='Alterar', bg='#87CEEB', activebackground='#87CEEB', activeforeground='black', command=self.alterar)
        alterar_bt.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.2)

    def apagar_veiculo(self):
        framea2 = Frame(self.aba2, bg='aliceBlue')
        framea2.place(relx=0, rely=0, relwidth=1, relheight=1)

        codigo_lb = Label(framea2, text='Código:', bg='AliceBlue')
        codigo_lb.place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.2)
        self.codigo_et = Entry(framea2, highlightbackground='gray', highlightthickness=2, validate='key',
                               validatecommand=self.valcod)
        self.codigo_et.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.2)

        comfirm_canvas = Canvas(framea2, bg='AliceBlue', bd=4, highlightbackground='Gray', highlightthickness=3)
        comfirm_canvas.place(relx=0.368, rely=0.59, relwidth=0.254, relheight=0.22)

        comfirmar_bt = Button(framea2, text='Confirmar', bg='#87CEEB', activebackground='#87CEEB',
                              activeforeground='white', command=self.fecharConta)
        comfirmar_bt.place(relx=0.37, rely=0.6, relwidth=0.25, relheight=0.2)

        confirm_balao = tix.Balloon(framea2)
        confirm_txt = 'Ao clicar, abre uma guia para fechar a conta do veiculo com o codigo correspondente ao do campo ao lado'
        confirm_balao.bind_widget(comfirmar_bt, balloonmsg=confirm_txt)

    def lista_veiculos(self):  # tabela
        frame3 = Frame(self.raiz, bg='AliceBlue', highlightbackground='gray', highlightthickness=3)
        frame3.place(relx=0.025, rely=0.55, relwidth=0.95, relheight=0.43)

        self.lista = ttk.Treeview(frame3, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.lista.heading('#0', text='')
        self.lista.heading('#1', text='código')
        self.lista.heading('#2', text='Placa')
        self.lista.heading('#3', text='Veiculo')
        self.lista.heading('#4', text='Data')
        self.lista.heading('#5', text='Horario de Entrada')

        self.lista.column('#0', width=10)
        self.lista.column('#1', width=170)
        self.lista.column('#2', width=130)
        self.lista.column('#3', width=220)
        self.lista.column('#4', width=150)
        self.lista.column('#5', width=150)
        self.lista.place(relx=0.025, rely=0.05, relwidth=0.925, relheight=0.9)

        barra = ttk.Scrollbar(frame3, orient='vertical')
        self.lista.configure(yscroll=barra.set)
        barra.place(relx=0.95, rely=0.05, relwidth=0.025, relheight=0.9)

        self.lista.bind('<Double-1>', self.DoubleLista)

    def menu(self):
        barramenu = Menu(self.raiz)
        self.raiz.configure(menu=barramenu)
        Menu1 = Menu(barramenu)
        Menu2 = Menu(barramenu)

        def sair():
            resp = messagebox.askquestion('Info', 'Tem certeza que deseja mesmo sair?')
            if resp:
                self.raiz.destroy()
            else:
                self.raiz.destroy()

        barramenu.add_cascade(label='Opções', menu=Menu1)
        barramenu.add_cascade(label='Detalhes', menu=Menu2)
        Menu1.add_command(label='Sair', command=sair)
        Menu2.add_command(label='Faturamento')


inter = Interface()
