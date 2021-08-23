from Aula002.Ex002.Carro import Carro

c1 = Carro()
c1.modelo = 'Camaro'
c1.cor = 'Amarelo'
c1.marca = 'Ford'
c1.placa = 'Ant0504'

print(c1.__dict__)

c2 = Carro()
c2.modelo = 'LaFerrari'
c2.cor = 'Vermelho'
c2.marca = 'Ferrari'
c1.placa = 'AnT0405'
print(c2.__dict__)