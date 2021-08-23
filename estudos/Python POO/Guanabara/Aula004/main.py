from Aula004.caneta import Caneta

c1 = Caneta()
c1.__setattr__('modelo', 'Bic')
c1.__setattr__('ponta', 0.5)
c1.__setattr__('cor', 'vermelho')
print(f'Eu tenho uma caneta {c1.getmodelo()} de ponta {c1.getponta()} e de cor {c1.getcor()} ')
print(c1.__getattribute__('cor'))


c2 = Caneta('Faber castel', 'preto', 0.5, 100, False)
print(c2.__dict__)

c3 = Caneta()
print(c2.__dict__)

