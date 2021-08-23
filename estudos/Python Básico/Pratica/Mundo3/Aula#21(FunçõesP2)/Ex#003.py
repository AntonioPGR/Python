def somar(a=0, b=0, c=0):
    """
    ->Faz a soma de até 3 numeros
    :param a: primeiro numero
    :param b: segundo numero
    :param c: terceiro numero
    :return: soma entre a b c
    """
    s = a + b + c
    return s


s1 = somar(5, 7, 9)
s2 = somar(6, 8, 9)

print(f'As somas valem {s1} e {s2}')