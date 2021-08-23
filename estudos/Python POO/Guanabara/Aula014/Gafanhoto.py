from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__experiencia = 0

    def GanharExperiencia(self):
        self.experiencia += 1

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

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, value):
        self.__experiencia = value


class Gafanhoto(Pessoa):
    def __init__(self, nome, idade, sexo, login):
        super().__init__(nome, idade, sexo)
        self.__login = login
        self.__totAssistido = 0

    def ViuMaisUm(self):
        self.totAssistido += 1

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def totAssistido(self):
        return self.__totAssistido

    @totAssistido.setter
    def totAssistido(self, value):
        self.__totAssistido = value
