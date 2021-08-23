valor = int(input('Qual o valor da casa?'))
salario = int(input('Qual o valor do seu salário?'))
anos = int(input('Em quantos anos desaja pagar?'))

np = anos*12
vp = valor/np
prcnt = 30/100*salario

print(prcnt, vp, np)
if vp > prcnt:
    print('O emprestimo não foi aprovado devivo ao valor do salário')
else:
    print('O emprestimo foi aprovado, você pagara R${:.2f} por mes durante {} meses'.format(vp,np))
