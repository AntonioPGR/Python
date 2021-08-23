galera = list()
dado = list()
for c in range(0,5):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
    else:
        print(f'{pessoa[0]} é menor de idade')