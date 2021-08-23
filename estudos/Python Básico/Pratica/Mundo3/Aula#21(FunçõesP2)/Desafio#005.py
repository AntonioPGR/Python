def notas(*num, sit=False):
    nota = dict()
    nota['total'] = len(num)
    nota['maior'] = max(num)
    nota['menor'] = min(num)
    nota['media'] = sum(num)/len(num)

    if sit == True:
        if nota['media'] > 7.5:
            nota['Situação'] = 'Boa'
        elif nota['media'] > 6:
            nota['Situação'] = 'Média'
        else:
            nota['Situação'] = 'Média'
    return nota


print(notas(12, 14, 16, 19, sit=True))
