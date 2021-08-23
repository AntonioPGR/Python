from animal import Animal


class Ave(Animal):
    def __init__(self, m, p, i, cp):
        super().__init__(m, p, i)
        self.__corPena = cp

    def locomover(self):
        print('voando')

    def alimentar(self):
        print('Comendo frutas')

    def emitirSom(self):
        print('Som de ave')

    def FazerNinho(self):
        print('Ninho feito')

    @property
    def corPena(self):
        return self.__corPena

    @corPena.setter
    def corPena(self, value):
        self.__corPena = value


class Arara(Ave):
    def __init__(self, m, p, i, cp):
        super().__init__(m, p, i, cp)
