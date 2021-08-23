vp = int(input('qual o valor do produto? '))
porc = int(input('de quantos porcento sera o desconto? '))
d = porc/100 * vp
print('o novo valor do produto é: {:.2f}'.format(vp-d))