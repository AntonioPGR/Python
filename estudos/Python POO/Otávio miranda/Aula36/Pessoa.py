from datetime import datetime

class Pessoa:
    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.anoAtual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano):
        idade = cls.anoAtual - ano
        return cls(nome, idade)

p1 = Pessoa.por_ano_nascimento('Antonio', 2006)
#p1 = Pessoa('Antonio', 14)
print(p1.nome, p1.idade)
