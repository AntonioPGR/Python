from typing import Type, Any


class Caneta:
    def __init__(self, mod='', cor='', pnt=0, carga=0, tampada=True):
        self.modelo = mod
        self.cor = cor
        self.ponta = pnt
        self.carga = carga
        self.tampada = tampada

    def settampada(self, v):
        self.tampada = v

    def gettampada(self):
        return self.tampada

    def getcor (self):
        return self.cor

    def setcor (self, v):
        self.cor = v

    def getponta(self):
        return self.ponta

    def setponta(self, v):
        self.ponta = v

    def getcarga(self):
        return self.carga

    def setcarga(self, v):
        self.carga = v

    def getmodelo(self):
        return self.modelo

    def setmodelo(self, v):
        self.modelo = v

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)





