def metade(p, form=True):
    if form:
        p = p / 2
        p = moeda(p)
        return p
    else:
        return p / 2


def dobro(p, form=True):
    if form:
        p = p*2
        p = moeda(p)
        return p
    else:
        return p * 2


def aumentar(p, porc=0, form=True):
    if form:
        aumento = (porc / 100) * p
        p += aumento
        p = moeda(p)
        return p
    else:
        aumento = (porc / 100) * p
        p += aumento
        return p


def diminuir(p, porc=0, form=True):
    if form:
        aumento = (porc / 100) * p
        p -= aumento
        p = moeda(p)
        return p
    else:
        aumento = (porc / 100) * p
        p -= aumento
        return p


def moeda(p, moed='R$'):
    p = f'{moed}{p:.2f}'.replace('.', ',')
    return p
