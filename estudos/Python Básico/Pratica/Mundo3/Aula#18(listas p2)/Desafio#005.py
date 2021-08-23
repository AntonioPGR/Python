from random import randint
from time import sleep
print('--'*20)
print('{:^35}'.format('Mega Sena'))
print('--'*20)
numjg = int(input('Quantos jogos você ira fazer? '))
jgs = list()
for c in range(0, numjg):
    jgs.append([])

print('--'*30)
print('{:^60}'.format(f'-=-=-=-=-Sorteando {numjg} jogos-=-=-=-=-'))
print('--'*30)
for i in range(0,numjg):
    sleep(1)
    for c in range(0,6):
        while True:
            numsort = randint(1, 60)
            if numsort not in jgs[i]:
                break
        jgs[i].append(numsort)
    print(f'Palpite numero {i+1}: {jgs[i]}')
print('<<<<< BOA SORTE >>>>>')
