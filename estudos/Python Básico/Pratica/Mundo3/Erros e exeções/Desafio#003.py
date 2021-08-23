from Ex003.Funcoes import Funcoes
from time import sleep

arq = "pessoas.txt"
if Funcoes.arqexist(arq) == False:
    arq = open('pessoas.txt', 'w')

while True:
    r = Funcoes.opcoes()
    if r == 3:
        break
