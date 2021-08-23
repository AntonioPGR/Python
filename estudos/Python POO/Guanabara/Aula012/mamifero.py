from animal import Animal


class Mamifero(Animal):
    def __init__(self, cp, m, p, i):
        super().__init__(m, p, i)
        self.__corPelo = cp

    def locomover(self):
        print('Correendo!!')

    def alimentar(self):
        print('Tomado leite!')

    def emitirSom(self):
        print('Som de mamifero!')

    @property
    def corPelo(self):
        return self.__corPelo

    @corPelo.setter
    def corPelo(self, value):
        self.__corPelo = value


class Canguru(Mamifero):
    def __init__(self, cp, m, p, i):
        super().__init__(cp, m, p, i)

    def usarBolsa(self):
        print('usando a bolsa')

    def locomover(self):
        print('Pulando')


class Cachorro(Mamifero):
    def __init__(self, m, p, i, cp):
        super().__init__(cp, m, p, i)

    def enterrarOsso(self):
        print('Enterrando osso')

    def abanarRabo(self):
        print('Abanando rabo')
