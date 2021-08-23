from Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, matr, curso, nome, idade, sexo):
        super().__init__(nome, idade, sexo)
        self.__matr = matr
        self.__curso = curso

    def cancelarMatricula(self):
        self.matr = 0
        self.curso = ''

    @property
    def mart(self):
        return self.__matr

    @property
    def curso(self):
        return self.__curso

    @mart.setter
    def mart(self, v):
        self.matr = v

    @curso.setter
    def curso(self, v):
        self.curso = v


class Bolsista(Aluno):
    def __init__(self, matr, curso, nome, idade, sexo, bolsa):
        super().__init__(matr, curso, nome, idade, sexo)
        self.__bolsa = bolsa

    def renovarBolsa(self,b):
        self.bolsa = b

    def PagarMensalidade(self, vt):
        print(f"Mensalidade paga! total: {vt - (self.bolsa/ 100 * vt)}")

    @property
    def bolsa(self):
        return self.__bolsa

    @bolsa.setter
    def bolsa(self, v):
        self.__bolsa = v


class Tecnico(Aluno):
    def __init__(self, matr, curso, nome, idade, sexo, registro):
        super().__init__(matr, curso, nome, idade, sexo)
        self.__registro = registro

    def praticar(self):
        print(f'Praticando {self.registro}')

    @property
    def registro(self):
        return self.__registro
