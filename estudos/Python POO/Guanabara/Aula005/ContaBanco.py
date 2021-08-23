class ContaBanco:

    def __init__(self):
        self.numconta = 0
        self.tipo = ''
        self.dono = ''
        self.saldo = 0.0
        self.status = False
    
    def AbrirConta(self, t):
        if self.getStatus() == True:
            print('A conta já foi aberta anteriormente!')
        elif t == 'cc':
            self.setTipo('cc')
            self.setSaldo(50)
            self.setStatus(True)
            print('Conta Corrente aberta com sucesso')
        elif self.getTipo() == 'cp':
            self.setTipo('cp')
            self.setSaldo(150)
            self.setStatus(True)
            print('Conta Poupança aberta com sucesso')
        else:
            print('tipo de conta invalido!')
            

    def FecharConta(self):
        if self.getStatus() == False:
            print('Você deve ter uma conta primeiro para poder fecha-la')
        elif self.getSaldo() != 0:
            if self.getSaldo() < 0:
                print('você deve pagar sua divida primeiro para poder fechar a conta')
            else:
                print('Você deve sacar todo o dinheiro da conta primeiro')
        else:
            self.setStatus(False)
            

    def Depositar(self, v):
        if self.getStatus() == False:
            print('Você deve ter uma conta já aberta para poder depositar!')
        else:
            self.setSaldo(self.getSaldo() + v)
    
    def sacar(self, v):
        if self.getStatus() == False:
            print('Você deve ter uma conta já aberta para poder sacar!')
        elif self.getSaldo() > v:
            self.setSaldo(self.getSaldo() - v)
        else:
            print('Saldo insuficiente!')

    def PagarMensal(self):
        if self.getStatus() == False:
            print('Você deve ter uma conta já aberta para poder sacar!')
        elif self.getTipo() == 'cc':
            self.setSaldo(self.getSaldo()-12)
        elif self.getTipo() == 'cp':
            self.setSaldo(self.getSaldo()-20)

    #Getter and Setter
    def getNumConta(self):
        return self.numconta
    def setNumConta(self, v):
        self.numconta = v

    def getTipo(self):
        return self.tipo
    def setTipo(self, v):
        self.tipo = v

    def getDono(self):
        return self.dono
    def setDono(self, v):
        self.dono = v

    def getSaldo(self):
        return self.saldo
    def setSaldo(self, v):
        self.saldo = v

    def getStatus(self):
        return self.status
    def setStatus(self, v):
        self.status = v