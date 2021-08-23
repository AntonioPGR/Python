matrix = [[], [], []]
somap = soma3 = maior2 = 0
for c in range(0,3):
    for i in range(0,3):
        num = int(input(f'Digite o numero da posição {c}, {i}: '))
        matrix[c].append(num)
        if num%2 == 0:
            somap += num
        if i == 2:
            soma3 += num
        if c == 1 and num > maior2:
            maior2 = num

print('-='*30)
for c in matrix:
    for i in range(0,3):
        print(f'[{c[i]:^5}] ', end=' ')
    print('')

print('-='*30)
print(f'''A soma dos valores pares é: {somap}
A soma dos valores da 3 coluna é {soma3}
O maior valor da 2 linha é {maior2}''')