def area(larg, comp):
    print(f'A area do seu terreno de {larg}x{comp} é de {larg*comp}m2')


l = float(input('Largura do terreno (m):'))
c = float(input('Comprimento do terreno (m):'))
area(l, c)