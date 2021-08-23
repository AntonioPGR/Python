def metade(p, form=True):
    if form:
        p = p/2
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


def resumo(p, menos=0, mais=0):
    print('-'*29)
    print(f'{"Resumo Do Valor":^29}')
    print('-'*29)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p)}')
    print(f'metade do preço: \t{metade(p)}')
    print(f'{mais}% de aumento: \t{aumentar(p, mais)}')
    print(f'{menos}% de desconto: \t{diminuir(p, menos)}')