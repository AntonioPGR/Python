from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6),
             'Jogador5': randint(1, 6)}

ranking = list()

print('-='*20)
print(f'{"Sorteando Valores":^20}')
print('-='*20)
for k, v in jogadores.items():
    sleep(0.5)
    print(f'O {k} tirou {v} no dado')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('--'*20)
print('Rank')
print('--'*20)
for i, v in enumerate(ranking):
    print(f'  -{i+1}o.: {v[0]}, que tirou {v[1]}')