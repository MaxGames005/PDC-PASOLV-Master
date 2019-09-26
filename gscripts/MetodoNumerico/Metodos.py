# Metodos Numericos
from extensoes.Dependencies import *


"""
Classe de Solucão de funçoes atraves da raiz encontrada no F(x) = 0
Utilizando Metodos Numericos Convencionas Como Metodo de Jacob, Newton e Regula-Falsi
"""


class MetodosNumericos:
    def __init__(self):
        """
        Inicializa as Variaveis e indices , tabem como funções aplicadas a partir de lambda
        utilização de funções ainda esta instavel não é recomendado o uso de UI para
        Utilizar das Capacidade da Classe
        """
        self.function = None
        self.xi = []
        self.xidx = []
        self.fidx = []
        self.idx = 0
        self.resultado = None
        self.ei = inf
        self.erro = 0

    def Newton(self):
        if self.xi and self.function:
            while self.ei > self.erro:
                try:
                    self.xidx.append((self.xidx[self.idx] * self.function(self.xidx[self.idx + 1])
                                      - self.xidx[self.idx + 1] * self.function(self.xidx[self.idx])) /
                                     (self.function(self.xidx[self.idx + 1]) -
                                      self.function(self.xidx[self.idx])))
                    self.idx += 1
                    if self.xidx[self.idx + 1]:
                        self.ei = self._erro(self.xidx[self.idx + 1], self.xidx[self.idx])
                    else:
                        print("fora de escopo")
                except:
                    print("Divergent")
                    break
            if not self.function(self.xidx[-1]):
                self.resultado = self.xidx[-1], self.ei, self.idx - 1
            else:
                self.resultado = "Fuckin _error", self.ei, self.idx - 1

    def RegulaFalsi(self):
        if self.xi and self.function:
            while self.ei > self.erro:
                try:
                    self.xidx.append((self.xidx[self.idx] * self.function(self.xidx[self.idx + 1])
                                      - self.xidx[self.idx + 1] * self.function(self.xidx[self.idx])) /
                                     (self.function(self.xidx[self.idx + 1]) -
                                      self.function(self.xidx[self.idx])))
                    self.idx += 1
                    if self.xidx[self.idx + 1]:
                        self.ei = self._erro(self.xidx[self.idx + 1], self.xidx[self.idx])
                    else:
                        print("fora de escopo")
                    if self.function(self.xidx[self.idx + 1]) * self.function(self.xidx[self.idx]) > 0:
                        aux = self.xidx[self.idx + 1]
                        self.xidx[self.idx + 1] = self.xidx[self.idx]
                        self.xidx[self.idx] = aux
                except:
                    print("Divergent")
                    break
            if not self.function(self.xidx[-1]):
                self.resultado = self.xidx[-1], self.ei, self.idx - 1
            else:
                self.resultado = "Fuckin _error", self.ei, self.idx - 1

    def Jacob(self):
        if self.xi and self.function:
            pass

    def addXi(self, x):
        self.xi = x
        self.xidx = self.xi

    def addF(self, f):
        self.function = f

    def _erro(self, x1, x0):
        return (((x1 - x0) / x1)**2)**0.5


"""
=================================================

== W = {(x,y,z,t) pt R4| x + y = 0 & z - t = 0}===
== U = {(x,y,z,t) pt R4| 2x + y - t = 0 e z = 0}==

=================================================

w|t = z
w|z = t
w|y = -x
w|x = x

=================================================


u|t = y + 2x
u|z = 0
u|y = t - 2x

x | 1  0  0  0 |
y |-2  0  0  1 |
t | 2  1  0  0 |

x    | 1  0  0  0 |
y+2x | 0  0  0  1 |
t-2x | 0  1  0  0 |

x = x
y + 2x = t
t - 2x = y



====================================================

W = {(1, -1, 1, 1), (0, 0, 1, -1), (-1, 1, 0, 0)}
U = {(0, 1, 0, 1), (1, -2, 0, 0)}
====================================================

u + u1 = (1, -2, 0, 0) + (0, 2, 0, 2)
w + w1 = (1, -1, 1, 1) + (0, 0, 1, -1)
W = (1 + 0) + (-1+0) = (1 + -1) + (0 + 0) = 0 + 0 = 0
W = (wx0 + wx1) + (wy0 + wy1) = (wx0 + wy0) + (wx1 + wy1)
U = 2*(0 + 1) + (1 - 2) - (1 + 0) = 2 - 1 - 1 = 0
U = 2*(ux0 + ux1) + (uy0 + uy1) - (ut0 + ut1) = 0


=====================================================


a*u = (a, -a, a, a) + (-a, a, 0, 0) + (0, 0, a, a)
b*w = (2b, -3b, b, b) + (-b, 2b, 0, b) + (b, -b, b, 2b)

"""
