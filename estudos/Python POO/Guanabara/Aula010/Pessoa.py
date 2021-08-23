class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    def FazerAniversario(self):
        self.idade += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def sexo(self):
        return self.__sexo

    @nome.setter
    def nome(self, v):
        self.__nome = v

    @idade.setter
    def idade(self, v):
        self.__idade = v

    @sexo.setter
    def sexo(self, v):
        self.__sexo = v