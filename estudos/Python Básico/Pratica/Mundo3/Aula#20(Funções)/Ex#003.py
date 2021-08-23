def dobra(lst):
    for i, v in enumerate(lst):
        lst[i] = v*2


valores = [6, 7, 3, 4, 5]
dobra(valores)
print(valores)