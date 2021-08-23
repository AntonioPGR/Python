from Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, setor, trab, nome, idade, sexo):
        super().__init__(nome, idade, sexo)
        self.__setor = setor
        self.__trabalhando = trab

    def mudarTrabalho(self, v):
        self.setor = v

    @property
    def setor(self):
        return self.__setor

    @property
    def trabalhando(self):
        return self.__trabalhando

    @setor.setter
    def setor(self, v):
        self.__setor = v

    @trabalhando.setter
    def trabalhando(self, v):
        self.__trabalhando = v