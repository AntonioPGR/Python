from Aula002.Ex001.caneta import Caneta

c1 = Caneta()
c1.modelo = 'Bic Cristal'
c1.cor = 'Azul'
c1.carga = 90
c1.ponta = 0.5
c1.tampada = False
c1.rabiscar()
c1.tampar()
print(c1.__dict__)

c2 = Caneta()
c2.modelo = 'Faber Castel'
c2.cor = 'Vermelha'
c2.carga = 50
c2.ponta = 1.0
c2.tampada = True
c2.destampar()

print(c2.__dict__)

