tot = s = 0
while True:
    n = int(input('Digite um valor:'))
    if n == 999:
        break
    s += n
    tot += 1
print(f'O numero de valores digitados é {tot} e a soma é {s} ')