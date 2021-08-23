def leiaDinheiro(quest):
    while True:
        p = str(input(quest)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print('\033[31mERRO! use apenas valores numéricos!\033[m')
        else:
            return float(p)