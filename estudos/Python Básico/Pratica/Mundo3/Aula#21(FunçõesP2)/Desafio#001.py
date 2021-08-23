def voto(nsc):
    from datetime import date
    idd = date.today().year - nsc
    if idd < 16:
        return f'Com {idd} anos o voto é proibido'
    elif idd < 18 or idd > 64:
        return f'Com {idd} anos o voto é opicional'
    else:
        return f'Com {idd} anos o voto é obrigatorio'


ano = int(input('Em que ano você nasceu?'))
print(voto(ano))
