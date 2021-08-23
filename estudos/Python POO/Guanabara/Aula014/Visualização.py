class Visualizacao():
    def __init__(self, espectador, filme):
        self.__espectador = espectador
        self.__filme = filme

    def avaliar(self, av):
        self.filme.avaliacao = av

    def avaliarNota(self, nt):
        self.filme.avaliacao = nt

    def AvaliarPorc(self, porc):
        self.filme.avaliacao = porc

    @property
    def espectador(self):
        return self.__espectador

    @espectador.setter
    def espectador(self, value):
        self.__espectador = value

    @property
    def filme(self):
        return self.__filme

    @filme.setter
    def filme(self, value):
        self.__filme = value
