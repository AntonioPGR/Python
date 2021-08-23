import datetime

pessoa = dict()
pessoa['nome'] = str(input('Nome:'))
anonasc = int(input('Ano de nascimento:'))
pessoa['idade'] = datetime.date.today().year - anonasc
pessoa['ctps'] = int(input('Carteira de trabalho: (0 para caso não tenha) '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação:'))
    pessoa['sal'] = int(input('Salario:'))

pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - anonasc

for k, v in pessoa.items():
    print(f'O {k} tem o valor {v}')