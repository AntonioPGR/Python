print('==='*10)
print('{:^30}'.format('Banco APGR'))
print('==='*10)
v = int(input('Qual Valor deseja sacar? R$'))
#var
n50 = n20 = n10 = n1 = 0
while True:
    if v >= 50:
        n50 += 1
        v -= 50
    elif v >= 20:
        n20 += 1
        v -= 20
    elif v >= 10:
        n10 += 1
        v -= 10
    elif v >= 1:
        n1 += 1
        v -= 1
    elif v == 0:
        break
print('==='*10)
if n50 > 0:
    print(f'Foram retiradas {n50} notas de R$50')

if n20 > 0:
    print(f'Foram retiradas {n20} notas de R$20')

if n10 > 0:
    print(f'Foram retiradas {n10} notas de R$10')

if n1 > 0:
    print(f'Foram retiradas {n1} notas de R$1')

print('O \033[1;32mBanco APGR\033[m agradece sua preferência')
#print(v)
#print(n50,n20,n10,n1)