nome = str(input('qual seu nome?'))
if nome.lower() == 'gustavo':
    print('Que nome feio você tem!')
elif nome.lower() == 'antonio':
    print('Que nome lindo você tem!')
elif nome.lower() in 'ana cláudia jéssica juliana':
    print('Que belo nome feminino você tem!')
else:
    print('Seu nome é bem normal.')
print('tenha um bom dia, {}!'.format(nome))