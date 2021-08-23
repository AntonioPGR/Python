matrix = [[], [], []]
for c in range(0,3):
    for i in range(0,3):
        num = int(input(f'Digite o numero da posição {c}, {i}: '))
        matrix[c].append(num)

for c in matrix:
    for i in range(0,3):
        print(f'[ {c[i]:^5} ]', end=' ')
    print('')