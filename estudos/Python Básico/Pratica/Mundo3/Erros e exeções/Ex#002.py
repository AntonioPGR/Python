try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dado que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por 0')
except KeyboardInterrupt:
    print('O usuario prefiriu não informar os valores')
except Exception as erro:
    print(f'O erro foi {erro.__class__}')
else:
    print(f'o resultado é {r:.2f}')
finally:
    print('<<Volte Sempre>>')