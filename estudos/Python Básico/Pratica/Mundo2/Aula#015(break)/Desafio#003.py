from random import randint
print('=-='*10)
print('Vamos jogar PAR ou IMPAR')
print('=-='*10)
#var:
pc = randint(0,10)
vit = 0
while True:
    n = int(input('Digite um valor:'))
    esc = str(input('Par ou impar? [P/I]')).upper().strip()[0]

    if esc == 'P':
        if (n+pc)%2 == 0:
            print('--' * 10)
            print(f'Você jogou {n} e o computador {pc}. a soma fica {n+pc}, então é PAR')
            print('--' * 10)
            print('Você venceu!!')
            vit += 1
        else:
            print('--' * 10)
            print(f'Você jogou {n} e o computador {pc}, a soma fica {n + pc} então é IMPAR')
            print('--' * 10)
            print('Você perdeu!')
            print('=-=' * 10)
            break
    elif esc == 'I':
        if (n+pc)%2 == 0:
            print('--' * 10)
            print(f'Você jogou {n} e o computador {pc}, a soma fica {n + pc} então é PAR')
            print('--' * 10)
            print('Você perdeu!')
            print('=-=' * 10)
            break
        else:
            print('--' * 10)
            print(f'Você jogou {n} e o computador {pc}. a soma fica {n + pc} então é IMPAR')
            print('--' * 10)
            print('Você venceu!!')
            vit += 1

    print('Vamos jogar novamente!')
    print('=-=' * 10)

print(f'Você teve {vit} vitorias')