listagem = ('Pão', 3.50,
            'Borracha', 1,
            'Carne', 30,
            'mochila', 120,
            'compasso', 9.99,
            'transferidor', 4.20,
            'chocolate', 5)
print('---'*10)
nome = 'Listagem de preços'
print('{:^30}'.format(nome))
print('---'*10)

for cn, c in enumerate(listagem):
    if cn%2 == 0:
        print(f'{c:.<25}', end= ' R$')
    else:
        print(f' {c:.2f}')
