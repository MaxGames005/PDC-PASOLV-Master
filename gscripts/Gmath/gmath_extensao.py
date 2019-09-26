# -*- coding: UTF-8 -*-
# MatBibli
from extensoes.Dependencies import *


def ln(x):
    """
    neperian logarithm function
    :param x: float
    :return: float
    """
    return log(x, e)


def plotar(XY, labelx, labely, title):
    X = XY[0]
    Yys = []
    for i in range(1, len(XY)):
        Yys.append(XY[i])
    for i in range(len(Yys)):
        plot(X, Yys[i])
    title(title)
    xlabel(labelx)
    ylabel(labely)
    legend()
    show()


def erro(x1, x0):
    try:
        y = (x1-x0)/x1
    except:
        y = inf
        return y
    return sqrt(pow(y, 2))


class MtdNum:
    def __init__(self):
        self.x0 = []
        self.x = []
        self.funcao = None
        self.idx = 0
        self.raiz = []
        self.erro = 0
        self.ei = inf
        self.steps = []

    def Newton(self):
        if self.x0 and self.funcao:
            self.idx = 0
            while self.ei > self.erro:
                self.x.append((self.x[self.idx]*self.funcao(self.x[self.idx+1]) -
                              self.x[self.idx+1]*self.funcao(self.x[self.idx])) /
                              (self.funcao(self.x[self.idx+1])-self.funcao(self.x[self.idx])))
                self.steps.append([self.x[self.idx+2], self.funcao(self.x[self.idx+2])])
                self.idx += 1
                self.ei = erro(self.x[self.idx+1], self.x[self.idx])
                if self.ei == inf:
                    print("Erro Não Existe Raiz No Intervalo")
            self.raiz = self.x[-1], self.ei, self.idx-1

    def Jacob(self):
        pass

    def RegulaFalsi(self):
        if self.x0 and self.funcao:
            while self.ei > self.erro:
                self.x.append((self.x[self.idx]*self.funcao(self.x[self.idx+1]) -
                              self.x[self.idx+1]*self.funcao(self.x[self.idx])) /
                              (self.funcao(self.x[self.idx+1])-self.funcao(self.x[self.idx])))
                self.idx += 1
                self.ei = erro(self.x[self.idx+1], self.x[self.idx])
                if self.funcao(self.x[self.idx])*self.funcao(self.x[self.idx+1]) > 0:
                    aux = self.x[self.idx+1]
                    self.x[self.idx+1] = self.x[self.idx]
                    self.x[self.idx] = aux
                if self.ei == inf:
                    print("Erro Não Existe Raiz No Intervalo")

            self.raiz = self.x[-1], self.ei, self.idx-1
        pass

    def add_xi(self, xi):
        self.x0 = xi
        self.x = self.x0

    def add_funcao(self, f):
        self.funcao = f






