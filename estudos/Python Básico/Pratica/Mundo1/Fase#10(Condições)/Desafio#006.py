n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))
n3 = int(input('Numero 3:'))

#maior:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

#menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior numero é {} e o menor é {}'.format(maior, menor))

#if n1 > n2 and n1 > n3:
    #print('O primeiro numero que é: {} é o maior numero.'.format(n1))
#else:
    #if n2 > n1 and n2 > n3:
        #print('O segundo numero que é: {} é o maior numero.'.format(n2))
    #else:
        #print('O terceiro numero que é: {} é o maior numero.'.format(n3))