from mamifero import Canguru, Cachorro
from reptil import Cobra, Tartaruga

print()
print('Canguru:')
c = Canguru('preto', 4, 85.2, 5)
c.locomover()
c.emitirSom()
c.alimentar()
c.usarBolsa()

# Reptil
print('--'*20)
print('Reptil:')
t = Tartaruga(30, 20, 4, 'verde')
t.locomover()
t.emitirSom()
t.alimentar()




