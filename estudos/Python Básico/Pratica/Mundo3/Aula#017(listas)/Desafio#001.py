val = []
for c in range(1,6):
    val.append(int(input(f'digite o valor para a posição {c}:')))

print(f'O maior valor é {max(val)} nas posições: ',end=' ')
for cn, c in enumerate(val):
    if c == max(val):
        print(f'{cn+1}...', end=' ')
print('')
print(f'O menor valor é {min(val)} nas posições: ', end=' ')
for cn, c in enumerate(val):
    if c == min(val):
        print(f'{cn+1}...', end= ' ')