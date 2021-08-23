import datetime

from imports import *


class Funcs:
    #  Banco de Dados:
    def conecta_bd(self):
        self.conn = sqlite3.connect('carros.bd')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def tabelaCarros(self):
        self.conecta_bd()
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS carros (
            id INTEGER PRIMARY KEY,
            placa CHAR(6) NOT NULL,
            modelo VARCHAR(30) DEFAULT '---------------',
            data TIMESTAMP NOT NULL 
        );
        """)
        self.conn.commit()
        self.desconecta_bd()
        self.mostrar_lista()

    def tabelaPrecos(self):
        self.conecta_bd()
        self.cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS precos (
        id INTEGER PRIMARY KEY,
        primeirahora INTEGER NOT NULL,
        segundahora INTEGER NOT NULL,
        demais INTEGER NOT NULL,
        gratis INTEGER NOT NULL
        );
        """)
        self.conn.commit()
        self.desconecta_bd()

    def dados(self):
        self.conecta_bd()
        self.cursor.execute("""
            SELECT primeirahora, segundahora, demais FROM precos WHERE id = 1;
        """)
        preco = self.cursor.fetchall()
        self.desconecta_bd()

        if not preco:
            self.conecta_bd()
            self.cursor.execute("""
                INSERT INTO precos ( primeirahora, segundahora, demais, gratis )
                VALUES ( 10, 5, 3, 10 )
            """)
            self.conn.commit()
            self.desconecta_bd()

    def mostrar_lista(self):
        self.lista.delete(*self.lista.get_children())
        self.conecta_bd()
        self.cursor.execute("""SELECT id, placa, modelo, data FROM carros ORDER BY placa""")
        carro = list(self.cursor.fetchall())
        for i in carro:
            i = list(i)
            i.append(str(f'{i[3][11:13]}:{i[3][14:16]}:{i[3][17:19]}'))
            i[3] = str(f'{i[3][8:10]}/{i[3][5:7]}/{i[3][:4]}')
            self.lista.insert("", END, values=i)
        self.desconecta_bd()

    #  adicionar veiculos
    def adicionar(self):
        if self.placa_et.get() == '':
            msg = 'Para adicionar o carro, você deve pelo menos informar a placa'
            messagebox.showinfo('Anthony Park - Info:', msg)
        else:
            placa = self.placa_et.get().upper()
            modelo = self.modelo_et.get()
            if modelo == '':
                modelo = '----------'

            data = datetime.now()

            self.conecta_bd()
            self.cursor.execute("""
                            INSERT INTO carros 
                            (placa, modelo, data)
                            VALUES
                            (?, ?, ?)
                            """, (placa, modelo, data))
            self.conn.commit()
            self.desconecta_bd()

            self.limpaTela()

            self.mostrar_lista()

    def ValidaEntradas(self):
        self.valcod = (self.raiz.register(self.ValidaCod), '%P')
        self.valPlaca = (self.raiz.register(self.ValidaPlaca), '%P')
        self.valModel = (self.raiz.register(self.ValidaModelo), '%P')

    def limpaTela(self):
        self.placa_et.delete(0, END)
        self.codigo_et.delete(0, END)
        self.modelo_et.delete(0, END)
        self.placaAlt_et.delete(0, END)
        self.idAlt_et.delete(0, END)
        self.modeloAlt_et.delete(0, END)

    #  Fechar Conta
    def deletar(self):
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM carros WHERE id = ?""", [self.idnum, ])
        self.conn.commit()
        self.desconecta_bd()

        self.mostrar_lista()

        self.root2.destroy()

    def fecharConta(self):
        self.idnum = self.codigo_et.get()
        self.codigo_et.delete(0, END)

        try:
            self.conecta_bd()
            self.cursor.execute("""DELETE FROM carros WHERE id = ?""", [self.idnum, ])
            self.desconecta_bd()
        except:
            msg = 'Para fechar conta, você deve informar o código do veiculo valido'
            messagebox.showinfo('Anthony Park - Info:', msg)
        else:
            self.Janela2(self.idnum)

    def CalcularPreco(self, idnum):
        def strptimedelta(Y: str = False, m: str = False, d: str = False, H: str = '00', M: str = '00', S: str = '00'):
            if not Y and not m and not d:
                return datetime.strptime(f'{H}:{M}:{S}', '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')
            elif not Y and not m:
                return datetime.strptime(f'{d} {H}:{M}:{S}', '%d %H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')
            elif not Y:
                return datetime.strptime(f'{m}-{d} {H}:{M}:{S}', '%m-%d %H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')
            else:
                datetime.strptime(f'{Y}-{m}-{d} {H}:{M}:{S}', '%Y-%m-%d %H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S')

        self.setaVarCalc(idnum)
        p1hr = self.ddados[0][0]
        p2hr = self.ddados[0][1]
        pdemais = self.ddados[0][2]
        tempoGratis = self.ddados[0][3]

        agr = datetime.strptime(str(datetime.now())[:19], '%Y-%m-%d %H:%M:%S')
        entrada = datetime.strptime(self.dcarro[0][2][:19], '%Y-%m-%d %H:%M:%S')
        tempofkd = agr - entrada

        if tempofkd < strptimedelta(M=f'{tempoGratis}'):
            return 0
        elif tempofkd < strptimedelta(H='1', M='14', S='59'):
            return p1hr
        elif tempofkd < strptimedelta(H='2', M='14', S='59'):
            return p2hr
        else:
            print(tempofkd)
            tempofkd -= strptimedelta(H='2', M='14', S='59')
            v = 15
            while tempofkd > strptimedelta(H='1'):
                tempofkd -= strptimedelta(H='1')
                v += 3
            return v

    def setaVarCalc(self, id):
        self.conecta_bd()
        self.cursor.execute("""
        SELECT placa, modelo, data FROM carros WHERE id = ?
        """, [id, ])
        self.dcarro = self.cursor.fetchall()
        self.cursor.execute("""
        SELECT primeirahora, segundahora, demais, gratis FROM precos WHERE id = 1;
        """)
        self.ddados = self.cursor.fetchall()
        self.desconecta_bd()

    def Janela2(self, cod):
        self.root2 = Toplevel()
        self.root2.title('Pagamento')
        self.root2.geometry('400x200')
        self.root2.resizable(False, False)
        self.root2.configure(bg='#1E90FF')
        self.root2.transient(self.raiz)
        self.root2.focus_force()
        self.root2.grab_set()

        v = self.CalcularPreco(cod)

        frame = Frame(self.root2, bg='AliceBlue')
        frame.place(relx=0.025, rely=0.05, relwidth=0.95, relheight=0.4)

        placa_fx = Label(frame, text='Placa:', bg='AliceBlue', font='Arial', anchor='w', fg='#1E90FF')
        placa_fx.place(relx=0.05, rely=0.1, relwidth=0.12, relheight=0.15)
        placa_md = Label(frame, text=self.dcarro[0][0], bg='AliceBlue', font='Arial', anchor='w')
        placa_md.place(relx=0.18, rely=0.1, relwidth=0.2, relheight=0.15)

        modelo_fx = Label(frame, text='Modelo:', bg='AliceBlue', font='Arial', anchor='w', fg='#1E90FF')
        modelo_fx.place(relx=0.05, rely=0.425, relwidth=0.15, relheight=0.15)
        modelo_md = Label(frame, text=self.dcarro[0][1], bg='AliceBlue', font='Arial', anchor='w')
        modelo_md.place(relx=0.21, rely=0.425, relwidth=0.7, relheight=0.15)

        horario_fx = Label(frame, text='Hora de entrada:', bg='AliceBlue', font='Arial', anchor='w', fg='#1E90FF')
        horario_fx.place(relx=0.05, rely=0.75, relwidth=0.32, relheight=0.15)
        horario_md = Label(frame, text=self.dcarro[0][2][10:16], bg='AliceBlue', font='Arial', anchor='w')
        horario_md.place(relx=0.37, rely=0.75, relwidth=0.2, relheight=0.15)

        comfirm_bt = Button(frame, text='Confirmar Pagamento', bg='#87CEEB',
                            activebackground='#87CEEB', activeforeground='white', command=self.deletar)
        comfirm_bt.place(relx=0.6, rely=0.325, relwidth=0.35, relheight=0.35)

        # Frame2:------------------------------------------------------------------------

        frame2 = Frame(self.root2, bg='AliceBlue')
        frame2.place(relx=0.025, rely=0.5, relwidth=0.45, relheight=0.45)

        tolerancia = Label(frame2, text=f'Tolerância: {self.ddados[0][3]} minutos', bg='AliceBlue', anchor='w')
        tolerancia.place(relx=0.01, rely=0.1, relwidth=0.99, relheight=0.17)

        hr1 = Label(frame2, text=f'1 hora: R${self.ddados[0][0]},00', bg='AliceBlue', anchor='w')
        hr1.place(relx=0.01, rely=0.3, relwidth=0.99, relheight=0.17)

        hr2 = Label(frame2, text=f'2 hora: R${self.ddados[0][1]},00', bg='AliceBlue', anchor='w')
        hr2.place(relx=0.01, rely=0.5, relwidth=0.99, relheight=0.17)

        demais = Label(frame2, text=f'Demais horas: R${self.ddados[0][2]},00', bg='AliceBlue', anchor='w')
        demais.place(relx=0.01, rely=0.7, relwidth=0.99, relheight=0.17)

        # Frame3:------------------------------------------------------------------------

        frame3 = Frame(self.root2, bg='AliceBlue')
        frame3.place(relx=0.525, rely=0.5, relwidth=0.45, relheight=0.45)

        preco = Label(frame3, text='Preço Final', bg='AliceBlue', font='Arial')
        preco.place(relx=0.01, rely=0.05, relwidth=0.99, relheight=0.17)

        total = Label(frame3, text=f'R${v}', bg='AliceBlue', font='Arial', fg='Blue')
        total.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

        menubar = Menu(self.root2)
        self.root2.configure(menu=menubar)
        menu1 = Menu(menubar)

        menubar.add_cascade(label='Opções', menu=menu1)
        menu1.add_cascade(label='Ficha do cliente')

    #  alterar
    def alterar(self):
        if not self.validaAlt():
            return

        placa = self.placaAlt_et.get()
        modelo = self.modeloAlt_et.get()
        idnum = self.idAlt_et.get()

        try:
            self.conecta_bd()
            vals = self.cursor.execute("""SELECT placa, modelo FROM carros WHERE id = ?""", [idnum, ]).fetchall()
            self.conn.commit()
            self.desconecta_bd()
        except:
            messagebox.showerror('Anthony Park Error', 'Error, id não encontrado, verifique o id e tente novamente')
            return

        if placa == '':
            placa = vals[0][0]
        elif modelo == '':
            modelo = vals[0][1]

        self.conecta_bd()
        self.cursor.execute("""UPDATE carros
                            SET modelo = ?, placa = ?
                            WHERE id = ?;
                            """, (modelo, placa, idnum))
        self.conn.commit()
        self.desconecta_bd()
        self.mostrar_lista()
        self.limpaTela()

    def validaAlt(self):
        placa = self.placaAlt_et.get()
        idnum = self.idAlt_et.get()
        vcomand = 0

        if len(placa) == 0 or len(placa) == 7:
            vcomand += 1
        if idnum.isnumeric():
            vcomand += 1
        if vcomand == 2:
            return True
        else:
            return False

    #  Eventos
    def DoubleLista(self, event):
        self.limpaTela()
        self.lista.selection()

        for el in self.lista.selection():
            col1, col2, col3, col4, col5 = self.lista.item(el, 'values')
            self.codigo_et.insert(END, col1)
            self.idAlt_et.insert(END, col1)
            self.placaAlt_et.insert(END, col2)
            self.modeloAlt_et.insert(END, col3)
