def leiaint():
    while True:
        try:
            num = int(input('Digite um numero inteiro: '))
        except KeyboardInterrupt:
            print('\033[31mO usuario prefiriu não digitar esse valor!')
            num = 0
            return num
        except:
            print('\033[31mERROR Digite apenas um numero inteiro valido!\033[m')
        else:
            return num


def leiafloat():
    while True:
        try:
            num = float(input('Digite um numero Real: '))
        except KeyboardInterrupt:
            print('\033[31mO usuario prefiriu não digitar esse valor!')
            num = 0
            return num
        except:
            print('\033[31mERROR, Digite apenas um numero real valido\033[m')
        else:
            return num


#programa principal
i = leiaint()
f = leiafloat()
print(f'O valore inteiro digitado foi {i} e o real foi {f}')