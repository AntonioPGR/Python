
jogador = dict()
jogadores = list()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    totgol = 0

    jogador['nome'] = input('Nome do jogador:')
    njgs = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0,njgs):
        gol = int(input(f'Quantos gols {jogador["nome"]} fez na partida {c+1}? '))
        gols.append(gol)
        totgol += gol

    jogador['gols'] = gols.copy()
    jogador['total'] = totgol
    jogador['Partidas'] = njgs

    jogadores.append(jogador.copy())

    if str(input('Deseja continuar? '))[0].strip().upper() == 'N':
        break

print('-='*30)
print(f'{"No.":<4} {"Nome":<10} {"No. Jogos":^15} {"gols":^20} {"total":>10}')
for count in range(0, len(jogadores)):
    print(f'{count} {jogadores[count]["nome"]} {jogadores[count]["Partidas"]} {jogadores[count]["gols"]} {jogadores[count]["total"]}')

print('-='*30)

while True:
    while True:
        jgdor = int(input('Deseja mostrar de algum jogador separadamente? (-1 encerra) '))
        if jgdor == -1:
            break
        elif jgdor >= 0 and jgdor < len(jogadores):
            break
        else:
            print('Nãoi temos nenhum jogador numerado com esse numero! por favor tente novamente')
    if jgdor == -1:
            break

    print(f'Levantamento do jogador {jogadores[jgdor]["nome"]}')
    for c in range(0, jogadores[jgdor]['Partidas']):
        print(f'Na partida {c+1} ele fez {jogadores[jgdor]["gols"][c]}')
    print(f'No total foram {jogadores[jgdor]["total"]} de gols')
    print('-=' * 30)

print('<<<Volte sempre >>>')
