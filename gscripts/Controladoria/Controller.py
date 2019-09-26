# Controller
from Extensoes.Dependencies import *

"""
Classe de Calculo de Finanças e Bases da Controladoria
"""


class Controladoria:
    def __init__(self):
        self.A = []
        self.Rn = [0]
        self.i = 0
        self.Vp = []
        self.J = [0]
        self.t = 0

    def SAC(self):
        self.A.append(0)
        for i in range(1, self.t + 1):
            self.A.append(self.Vp[0] / self.t)
            self.J.append((self.Vp[-1]) * self.i)
            self.Rn.append(self.J[-1] + self.A[-1])
            self.Vp.append(self.Vp[-1] - self.Rn[-1])

    def Price(self):
        pass

    def Tempo(self, tempo):
        self.t = tempo

    def Taxa(self, taxa):
        self.i = taxa

    def Exibir(self):
        for i in range(1, self.t + 1):
            print([i - 1, self.Vp[i - 1], self.A[i - 1], self.J[i - 1], self.Rn[i - 1]])

    def SaldoDev(self, saldo):
        self.Vp.append(saldo)


"""
Usage:

Con = Controladoria()
Con.Tempo(120)
Con.Taxa(0.01)
Con.SaldoDev(60000)
Con.SAC()
Con.Exibir()
"""




