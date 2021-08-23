from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, m, p, i):
        self.__peso = p
        self.__membros = m
        self.__idade = i

    @abstractmethod
    def locomover(self):
        pass

    @abstractmethod
    def alimentar(self):
        pass

    @abstractmethod
    def emitirSom(self):
        pass

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    @property
    def membros(self):
        return self.__membros

    @membros.setter
    def membros(self, value):
        self.__membros = value

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, value):
        self.__idade = value
