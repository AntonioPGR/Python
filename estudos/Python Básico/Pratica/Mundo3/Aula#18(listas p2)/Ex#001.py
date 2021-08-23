teste = list()
teste.append('Antonio')
teste.append(14)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 21
galera.append(teste[:])
print(galera)