import math

a = float(input('Digite o valor do ângulo: '))
r = math.radians(a)
print('O angulo de {}° tem o SENO de: {:.2f} ;'.format(a, math.sin(r)))
print('O angulo de {}° tem o COSSENO de: {:.2f};'.format(a, math.cos(r)))
print('O angulo de {}° tem o TANGENTE de : {:.2f}'.format(a, math.tan(r)))