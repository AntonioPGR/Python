def metade(p):
    return p / 2


def dobro(p):
    return p * 2


def aumentar(p, porc=0):
    aumento = (porc / 100) * p
    p += aumento
    return p


def diminuir(p, porc=0):
    menos = (porc / 100) * p
    p -= menos
    return p


def moeda(p=0, moeda='R$'):
    p = f'{moeda:}{p:.2f}'.replace('.', ',')
    return p
