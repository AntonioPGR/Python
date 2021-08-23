from animal import Animal


class Peixe(Animal):
    def __init__(self, m, p, i, ce):
        super().__init__(m, p, i)
        self.__corEscama = ce

    def locomover(self):
        print('Nadando')

    def alimentar(self):
        print('Comendo algas')

    def emitirSom(self):
        print('Blup')

    def SoltarBolha(self):
        print('Bolha')
        self.emitirSom()

    @property
    def corEscama(self):
        return self.__corEscama

    @corEscama.setter
    def corEscama(self, value):
        self.__corEscama = value


class GoldFish(Peixe):
    def __init__(self, m, p, i, ce):
        super().__init__(m, p, i, ce)

