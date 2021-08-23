try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    r = a / b
except Exception as erro:
    print(f'[ERRO] Problema do tipo {erro.__class__}')
else:
    print(f'o resultado é {r:.2f}')
finally:
    print('<<Volte Sempre>>')
