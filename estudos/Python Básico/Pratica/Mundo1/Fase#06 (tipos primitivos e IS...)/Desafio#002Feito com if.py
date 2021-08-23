a = input('digite algo:')
if(a.isnumeric() == True):
    print(a,'é numérico')
else:
    if(a.isalpha() == True):
        print(a,'é caractere')
    else:
        print(a,'é alfanumérico');

if(a.isupper == True):
    print('e esta em maisusculo')
else:
    print('e esta em minusculo');
