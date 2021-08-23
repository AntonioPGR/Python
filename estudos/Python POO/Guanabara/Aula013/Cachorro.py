class Cachorro:
    def __init__(self, idd, peso):
        self.__idade = idd
        self.__peso = peso

    @staticmethod
    def reagirFrase(frase: str):
        if frase == 'amigavel':
            print('Abanar rabo e latir')
        else:
            print('rosnar')

    @staticmethod
    def reagirHora(hora: int):
        if 12 > hora > 6:
            print('Abanar o rabo')
        elif hora < 18:
            print('Brincar')
        else:
            print('ignorar')

    @staticmethod
    def reagirDono(dono: bool):
        if dono:
            print('Brincar')
        else:
            print('rosnar e latir')

    def reagirIdade(self):
        if self.idade <= 5 and self.peso < 15:
            print('abanar')
        elif self.idade <= 5 and self.peso > 15:
            print('latir')
        elif self.idade > 5 and self.peso < 15:
            print('rosnar')
        else:
            print('ignorar')


    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, value):
        self.__idade = value
