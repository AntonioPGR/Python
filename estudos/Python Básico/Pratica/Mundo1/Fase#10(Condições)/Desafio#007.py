s = float(input('Qual o salário do funcionario?'))

if s > 1250:
    s = s + (10/100 * s)
    print('O novo salário com aumento de 10% é:',s)
else:
    s = s + (15/100 * s)
    print('O novo salário com aumento de 15% é:',s)

