def chelp():
    r = input('\033[mFunção ou biblioteca >>: ')
    if r.strip().upper() == 'FIM':
        return 'T'
    else:
        lr = len(r) + 36
        print('\033[30;42m~'*lr)
        print(f"  Acessando o manual do comando '{r}'")
        print('~' * lr)
        print('\033[1;37;40m')
        print(help(r))


while True:
    print('\033[1;30;44m~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  Sistema de ajuda PyHelp')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    t = chelp()
    if t == 'T':
        break

print('Volte Sempre...')