frase = str(input('digite sua frase:')).strip().upper()
palavras = frase.split()
tdjnt = ''.join(palavras)
inverso = ''
for c in range(len(tdjnt)-1, -1, -1):
    inverso = inverso+tdjnt[c]

print('A frase {} ao contrario fica: {}'.format(tdjnt,inverso))
if tdjnt == inverso:
    print("Essa frase \033[36mé um palíndromo")
else:
    print('Essa frase \033[31mnão é um palíndromo')