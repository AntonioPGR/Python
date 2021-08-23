alunos = list()
dados = list()
nota = list()
while True:
    dados.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    dados.append(nota[:])
    alunos.append(dados[:])
    dados.clear()
    nota.clear()

    r = str(input('Deseja continuar? [s/n]'))[0].strip().upper()
    if r == 'N':
        break
#print(alunos)

print('-='*30)
print(f'{"no.":<4}{"nome":<10}{"media":>8}')
print('-'*30)
for num, nome in enumerate(alunos):
    media = (nome[1][0] + nome[1][1]) / 2
    print(f'{num:<4}{nome[0]:<10}{media:>8}')
print('-='*30)

while True:
    resp = int(input('Deseja ver a nota de qual aluno separadamente? (-1 interrompe)'))
    if resp == -1:
        break
    while True:
        if resp < 0 or resp > len(alunos)-1:
            print('Não temos nenhum aluno com esse numero!')
            print('-=' * 30)
            resp = int(input('Deseja ver a nota de qual aluno separadamente? (-1 interrompe)'))
        else: break
    print(f'A nota do aluno {alunos[resp][0]} é {alunos[resp][1][0]} e {alunos[resp][1][1]}')
    print('-=' * 30)
print(f'{"<<Encerrando sistema>>":^20}')