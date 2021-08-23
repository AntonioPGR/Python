pessoas = list()
dados = list()
maiorP = list()
menorP = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('peso:')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    r = str(input('Deseja continuar? '))[0].strip().upper()
    if r == 'N':
        break

print('-='*30)
print(f'Ao todo vc cadastrou {len(pessoas)} pessoas')
print(f'Os mais pesados foram: ', end=' e ')
for p in pessoas:
    if p[1] == maior:
        print(p[0],end=' ')
print(' ')

print(f'Os mais leves foram: ',end= ' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' e ')

