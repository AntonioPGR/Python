estado = dict()
brasil = list()

for c in range(0,2):
    print('-='*20)
    estado['uf'] = str(input('Unidade federativa:'))
    estado['sigla'] = str(input('Sigla:')).upper()
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(k, ':', v, end=' -- ')
    print()