def leiaint(frase):
    while True:
        num = str(input(frase))
        if num.isnumeric():
            int(num)
            break
        else:
            print('\033[31m[ERRO!]Digite apenas um valor \033[m')
    return num


n = leiaint('Digite um numero: ')
print(f'\033[34mVocê digitou {n}')