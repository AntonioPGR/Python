pessoas = list()
dados = dict()
mulheres = list()
acimamedia = list()
somaidd = 0
while True:
    print('-='*20)
    dados['nome'] = str(input('Nome:')).strip()
    dados['sexo'] = str(input('Sexo:'))[0].strip().upper()
    dados['idade'] = int(input('Idade:'))

    somaidd += dados['idade']

    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    pessoas.append(dados.copy())
    if str(input('quer continuar? [S/N]'))[0].strip().upper() == 'N':
        break

media = somaidd / len(pessoas)

print('-='*20)
print(f'temos {len(pessoas)} cadastradas;')
print(f'A média de idade é {media}')
print(f'As mulheres cadastradas são {mulheres}')

for num, elemento in enumerate(pessoas):
    if pessoas[num]['idade'] > media:
        acimamedia.append(pessoas[num].copy())

print(f'As pessoas com idade acima da média são:')
for v in acimamedia:
    for k,val in v.items():
        print(f'{k} = {val};',end=' ')
    print(' ')