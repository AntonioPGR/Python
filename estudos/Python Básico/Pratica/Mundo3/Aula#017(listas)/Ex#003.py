a = [2, 3, 4, 7]
#b = a # b cria uma ligação com a, td q eu mecher em um muda em ambos
#b[2] = 8
b = a[:]#b copia os itens de a
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')