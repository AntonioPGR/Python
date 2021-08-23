class Caneta:
    def __init__(self):
        self.modelo = ''
        self.cor = ''
        self.ponta = 0.0
        self.carga = 0
        self.tampada = False

    def rabiscar(self):
        if self.tampada:
            print('Destampe a caneta primeiro')
        else:
            print('rabiscando')

    def tampar(self):
        self.tampada = True
        print('tampada')

    def destampar(self):
        self.tampada = False
        print('destampada')
