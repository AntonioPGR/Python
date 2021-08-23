from time import sleep
pessoas = []

def titulo(txt):
    print('--' * 20)
    print(f'{txt:^40}')
    print('--' * 20)


def opcoes():
    while True:
        titulo('Menu Principal')
        print('\033[33m 1 \033[m- \033[35m Ver pessoas cadastradas \033[m')
        print('\033[33m 2 \033[m- \033[35m Cadastrar nova pessoa \033[m')
        print('\033[33m 3 \033[m- \033[35m fechar programa \033[m')
        print('--'*20)
        try:
            r = int(input('\033[33mSua opção: \033[m'))
        except:
            print('\033[31m ERROR: Digite apenas valores inteiros \033[m')
        else:
            if r <= 0 or r >= 4:
                print('\033[31m ERROR: Digite apenas opções validas validos \033[m')
            else:
                if r == 1:
                    Verpessoas()
                elif r == 2:
                    Addpessoas()
                else:
                    return r

def Verpessoas():
    titulo('Pessoas Cadastradas')
    arq = open('pessoas.txt', 'rt')
    print(f'\033[34m{"nome":<10}{"idade":>29}\033[m')
    for linha in arq:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'\033[33m{dado[0]:<10} \033[36m{dado[1]:>27}\033[m')



def Addpessoas():

    titulo('Adicionar Pessoas')
    while True:
        nome = str(input('\033[33mNome: \033[m'))
        if nome.isnumeric():
            print('\033[31mERROR! Digite apenas nomes validos!\033[m')
        else:
            break
    while True:
        try:
            idd = int(input('\033[33mIdade: \033[m'))
        except:
            print('\033[31mERROR! Digite apenas numeros inteiros!\033[m')
        else:
            break

    arq = open('pessoas.txt', 'a')
    arq.write(f'{nome};{idd}\n')

    print('\033[36mAdicionado com sucesso\033[m')

def arqexist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
