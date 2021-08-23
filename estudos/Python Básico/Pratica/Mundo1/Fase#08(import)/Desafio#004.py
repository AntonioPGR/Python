from random import choice
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
#nomes = [a1, a2, a3, a4]
print('O aluno escolhido é: {}'.format(choice([a1, a2, a3, a4])))