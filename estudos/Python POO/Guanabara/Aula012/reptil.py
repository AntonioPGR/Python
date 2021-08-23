from animal import Animal


class Reptil(Animal):
    def __init__(self, peso, idade, membros, corEscama):
        super().__init__(peso, idade, membros)
        self.__corEscama = corEscama

    def locomover(self):
        print('locomover')

    def alimentar(self):
        print('Comendo vegetais')

    def emitirSom(self):
        print('Som de reptil')

    @property
    def corEscama(self):
        return self.__corEscama

    @corEscama.setter
    def corEscama(self, value):
        self.__corEscama = value


class Cobra(Reptil):
    def __init__(self, peso, idade, membros, corEscama):
        super().__init__(peso, idade, membros, corEscama)


class Tartaruga(Reptil):
    def __init__(self, peso, idade, membros, corEscama):
        super().__init__(peso, idade, membros, corEscama)

    def locomover(self):
        print('Andando lentamente')
