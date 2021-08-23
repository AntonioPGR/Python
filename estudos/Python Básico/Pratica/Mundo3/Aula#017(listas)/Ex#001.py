num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #add 7
num.sort(reverse=True)#organiza em ordem crescente ou decrecente
num.insert(2,2)#na posi 2 inserir 2
num.remove(2)#remove o num 2, caso houver 2 elemento 2 ele remove o primeiro
if 5 in num:
    num.remove(5)
else:
    print('Não axei o numero 4')
#num.pop()#elimina o ultimo elemento
#num.pop(2)#elimina o elemento na posi 2
print(num)
print(f'Essa lista tem {len(num)} elementos')