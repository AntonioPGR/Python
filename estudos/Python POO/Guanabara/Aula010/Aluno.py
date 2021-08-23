from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, matr, curso, nome, idade, sexo):
        super().__init__(nome, idade, sexo)
        self.__matr = matr
        self.__curso = curso

    def cancelarMatricula(self):
        self.matr = 0
        self.curso = ''

    @property
    def mart(self):
        return self.__matr

    @property
    def curso(self):
        return self.__curso

    @mart.setter
    def mart(self, v):
        self.matr = v

    @curso.setter
    def curso(self, v):
        self.curso = v