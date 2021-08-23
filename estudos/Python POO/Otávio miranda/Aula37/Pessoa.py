from datetime import datetime
from random import randint

class Pessoa:
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): #muda algo da instancia, p1, p2
        print(self.anoAtual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano): #muda algo da classe, global
        idade = cls.anoAtual - ano
        return cls(nome, idade)

    @staticmethod
    def gera_id(): #não mexe na classe nem instancia
        return randint(10000, 99999)

p1 = Pessoa.por_ano_nascimento('Antonio', 2006)
#p1 = Pessoa('Antonio', 14)
print(p1.nome, p1.idade)
print(p1.gera_id())
