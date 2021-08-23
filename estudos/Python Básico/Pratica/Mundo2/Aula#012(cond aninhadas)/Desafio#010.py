from random import choice
from time import sleep
l = [0, 1, 2]
pc = choice(l)

usu = int(input("""Vamos jogar!!
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual sua escolha?
"""))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if usu == 0:
    escu = 'pedra'
elif usu == 1:
    escu = 'papel'
elif usu == 2:
    escu = 'tesoura'

if pc == 0:
    escp = 'pedra'
elif pc == 1:
    escp = 'papel'
elif pc == 2:
    escp = 'tesoura'


if pc == 0 and usu == 2 or pc == 2 and usu == 1 or pc == 1 and usu == 0:

    print('-*-' * 7)
    print('''Usuario: \033[2;34m{} \033[m
Computador: \033[2;33m{} \033[m'''.format(escu, escp))
    print('-*-' * 7)
    print('Você perdeu!!')

elif usu == 0 and pc == 2 or usu == 2 and pc == 1 or usu == 1 and pc == 0:

    print('-*-' * 7)
    print('''Usuario: \033[2;34m{} \033[m
Computador: \033[2;33m{} \033[m'''.format(escu, escp))
    print('-*-' * 7)
    print('Você ganhou!!')

elif usu == 0 and pc == 0 or usu == 2 and pc == 2 or usu == 1and pc == 1:

    print('-*-' * 7)
    print('''Usuario: \033[2;34m{} \033[m
Computador: \033[2;33m{} \033[m'''.format(escu, escp))
    print('-*-' * 7)
    print('Deu empate!!')

else:
    print('[ Erro ] Digite um numero valido')