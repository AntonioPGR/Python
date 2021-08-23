"""
_dados = privado mais fraco, ele esconde mas pode acessar
__dados = privado mais forte, proibe que acesse o metodo(private), mas pode-se acessar com _NomeDaClasse__Nome
tudo serve para functions e variaveis
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir(self, id, nome):
        if not 'clientes' in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'id = {id} // nome = {nome}')

    def apaga(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserir(1, 'Otávio')
bd.inserir(2, 'José')
bd.inserir(3, 'rose')
bd.apaga(2)
bd.lista()

"""Atributo criado com o mesmo nome, mas não é o atributo:"""
#bd.__dados = 'outra coisa'
#print(bd.__dados)

"""O real atributo está nesse aqui: instancia.nomedaclasse.atributo"""
#print(bd._BaseDeDados__dados)

print(bd.dados)


