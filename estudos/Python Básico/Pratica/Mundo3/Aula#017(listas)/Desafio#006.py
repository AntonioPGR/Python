ex = str(input('Digite uma expressão com parenteses:')).strip()
parente = []
for letras in ex:
    if letras == '(':
        parente.append('(')
    if letras == ')':
        parente.pop()

if parente == []: #´guanabara: len(parente) == 0
    print('Expressão valida!')
else:
    print('Expressão invalida!')
