from mamifero import Mamifero, Canguru
from reptil import Reptil
from Peixe import Peixe
from Ave import Ave

# mamifero
print('--'*20)
print('Mamifros:')
m = Mamifero('preto', 4, 85.2, 5)
m.locomover()
m.emitirSom()
m.alimentar()

# Reptil
print('--'*20)
print('Reptil')
r = Reptil()

# Peixe
print('--'*20)
print('Peixe')
p = Peixe(0, 0.550, 2, 'Azul')
p.locomover()
p.emitirSom()
p.alimentar()
p.SoltarBolha()

# Ave
print('--'*20)
print('Ave:')
a = Ave(2, 1, 1, 'Branco')
a.locomover()
a.emitirSom()
a.alimentar()
a.FazerNinho()




