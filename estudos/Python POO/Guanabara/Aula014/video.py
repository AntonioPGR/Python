from abc import ABC, abstractmethod


class AcoesVideo(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def like(self):
        pass

# ______________________________________________________________________________________

class Video(AcoesVideo):
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__avaliacao = 0
        self.__views = 0
        self.__curtidas = 0
        self.__reproduzindo = False

    def play(self):
        if self.reproduzindo:
            print('O video ja esta sendo reproduzido')
        else:
            self.reproduzindo = True
            self.views += 1

    def pause(self):
        if not self.reproduzindo:
            print('O video ja esta pausado')
        else:
            self.reproduzindo = False

    def like(self):
        self.curtidas += 1

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def avaliacao(self):
        return self.__avaliacao

    @avaliacao.setter
    def avaliacao(self, value):
        self.__avaliacao = value

    @property
    def views(self):
        return self.__views

    @views.setter
    def views(self, value):
        self.__views = value

    @property
    def curtidas(self):
        return self.__curtidas

    @curtidas.setter
    def curtidas(self, value):
        self.__curtidas = value

    @property
    def reproduzindo(self):
        return self.__reproduzindo

    @reproduzindo.setter
    def reproduzindo(self, value):
        self.__reproduzindo = value
