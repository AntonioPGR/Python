valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'posição {c} temos o valor: {v}')
print('cheguei ao final da lista')