def fatorial(num=1, show=False):
    """
    -> calcula o fatorial de um numero
    :param num: O numero a ser calculado o fatorial
    :param show: (opcional) Mostra ou não o fatorial na tela
    :return: O fatorial de num
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            if c == 1:
                print(f' {c}', end=' ')
            else:
                print(f' {c} x', end='')
    if show:
        print(f'= {fat}')
    return fat


print(fatorial(5, show=True))
help(fatorial)



