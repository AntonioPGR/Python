from random import randint
t = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram:',end=' ')
#maior = menor = t[0]
for cn,c in enumerate(t):
    print(t[cn], end=' ')
#    if t[cn] > maior:
#        maior = t[cn]
#    elif t[cn] < menor:
#        menor = t[cn]
print(' ')
print(f'Menor: {min(t)}')#menor numero da tupula
print(f'maior: {max(t)}')#maior da tupula


