from Modulos import *


class Funcoes:

    def variaveis(self):
        self.codigo = self.et_code.get()
        self.nome = self.et_nome.get()
        self.telefone = self.et_telefone.get()
        self.cidade = self.et_cidade.get()

    def limpaTela(self):
        self.et_code.delete(0, END)
        self.et_nome.delete(0, END)
        self.et_telefone.delete(0, END)
        self.et_cidade.delete(0, END)

    def add_cliente(self):
        self.variaveis()

        if self.nome == '':
            msg = 'Para cadastrar um novo cliente, é nescessário \n'
            msg += ' digitar pelo menos um nome'
            messagebox.showinfo("CAdastro de Clientes - Aviso:", msg)
        else:
            self.conecta_bd()
            self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
                VALUES(?, ?, ?)""", (self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpaTela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def montaTabelas(self):
        self.conecta_bd()
        # Crando Tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)        
        );
        """)
        self.conn.commit()
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpaTela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.et_code.insert(END, col1)
            self.et_nome.insert(END, col2)
            self.et_telefone.insert(END, col3)
            self.et_cidade.insert(END, col4)

    def deleta_cliete(self):
        self.variaveis()

        if self.codigo == '':
            msg = 'Para apagar o cliente, digite pelo menos seu código'
            messagebox.showinfo('Cadastro de clientes - Aviso!', msg)
        else:
            self.conecta_bd()

            self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", [self.codigo, ])
            self.conn.commit()

            self.desconecta_bd()
            self.limpaTela()
            self.select_lista()

    def altera_cliente(self):
        self.variaveis()

        if self.codigo == '':
            msg = 'Para alterar o cliente, digite pelo menos seu código'
            messagebox.showinfo('Cadastro de clientes - Aviso!', msg)
        else:
            self.conecta_bd()
            self.cursor.execute("""UPDATE clientes
            SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpaTela()

    def buscar(self):
        self.variaveis()

        if self.codigo == '':
            msg = 'Para buscar o cliente, digite pelo menos seu código'
            messagebox.showinfo('Cadastro de clientes - Aviso!', msg)
        else:
            self.conecta_bd()
            self.listaCli.delete(*self.listaCli.get_children())
            self.et_nome.insert(END, '%')
            nome = self.et_nome.get()
            print(nome)
            self.cursor.execute("""SELECT * FROM clientes WHERE nome_cliente LIKE '%s'
            ORDER BY nome_cliente ASC""" % nome)
            pessoas = self.cursor.fetchall()
            self.conn.commit()

            for itens in pessoas:
                self.listaCli.insert('', END, values=itens)

            self.desconecta_bd()
            self.limpaTela()

    def imagens_base64(self):
        self.btnovo_base64 = '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'

    def calendario(self):
        self.calendario1 = Calendar(self.aba2, fg='gray75', bg='blue', font=('Times', '9', 'bold'), locale='pt_br')
        self.calendario1.place(relx=0.5, rely=0.1)
        self.callData = Button(self.aba2, text='Inserir Data', command=self.print_call)
        self.callData.place(relx=0.8, rely=0.85, height=25, width=100)

    def print_call(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.data_et.delete(0, END)
        self.data_et.insert(END, dataIni)
        self.callData.destroy()
