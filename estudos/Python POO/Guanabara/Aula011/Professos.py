from Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, esp, sal, nome, idade, sexo):
        super().__init__(nome, idade, sexo)
        self.__especialidade = esp
        self.__salario = sal

    def aumento(self, v):
        self.salario += v

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def salario(self):
        return self.__salario

    @especialidade.setter
    def especialidade(self, v):
        self.__especialidade = v

    @salario.setter
    def salario(self, v):
        self.__salario = v