from Pessoa import Pessoa


class Visitante(Pessoa):
    def __init__(self, nome, idade, sexo):
        super().__init__(nome, idade, sexo)