from typing import List, Any

jogador = dict()
gols = list()
jogador['nome'] = input('Nome do jogador:')
njgs = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
totgol = 0

for c in range(0,njgs):
    gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {c+1}? '))
    gols.append(gol)
    totgol += gol

jogador['gols'] = gols.copy()
jogador['total de gols'] = totgol
jogador['Partidas'] = njgs

print('-='*30)
print('Informações do jogador')
print('-='*30)

for k, v in jogador.items():
    print(f'{k}: {v}')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {jogador["Partidas"]} partidas:')
for c in range(0,jogador['Partidas']):
    print(f'=> na partida {c+1}, ele fez {jogador["gols"][c]}')
print(f'O total de gols foi: {jogador["total de gols"]}')