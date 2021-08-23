p = ('treinar', 'python', 'curso', 'guanabra', 'aprender','programar','linguagem')
#cn = numero palavra, i == numero letra, c = palavra
for cn, c in enumerate(p):
    print(f'Na palavra {c} temos as vogais:', end= ' ')
    for i in range(0, len(p[cn])):
        if p[cn][i] == 'a' or p[cn][i] == 'e' or p[cn][i] == 'i' or p[cn][i] == 'o' or p[cn][i] == 'u':
            print('\033[34m'+p[cn][i]+'\033[m', end=' ')
    print('')