def contador(i, f, p):
    """
    -> Faz uma contagem e mostra ela na tela
    :param i: inicio
    :param f: fim
    :param p: passo
    :return: sem retorno
    Created by Antonio Pacheco
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')


help(contador)
