pessoas = {'nome': 'Antonio', 'sexo':'M', 'idade': 14}
#for k in pessoas.keys():
#    print(k)
#for v in pessoas.values():
#    print(v)
#del pessoas['sexo']
#pessoas['nome'] = 'Gustavo'
pessoas['peso'] = 72
for k, v in pessoas.items():
    print(f'{k}: {v}')