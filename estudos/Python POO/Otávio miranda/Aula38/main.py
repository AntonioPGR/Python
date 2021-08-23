class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, desc):
        self.preco = self.preco - (self.preco * (desc /100))
        self.preco = float(self.preco)

    #Getter
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return  self._nome

    #Setter
    @preco.setter
    def preco(self, v):
        if isinstance(v, str):
            v = float(v.replace('R$', ''))
        self._preco = v

    @nome.setter
    def nome(self, v):
        self._nome = v

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

