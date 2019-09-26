# Mecanica
from extensoes.Dependencies import *


# V0^2 + 2aS = V^2
# V^2 - 2aS = V0^2
# (V^2 - V0^2)/2a = S
# (V^2 - V0^2)/2S = a


class Torricelli:
    def __new__(cls, *args):
        instance = super(Torricelli, cls).__new__(cls)
        instance.__init__(*args)
        idx = []
        for i in range(len(args)):
            if args[i] == None:
                idx.append(i)
        V0 = args[0]
        V1 = args[1]
        a = args[2]
        S = args[3]
        if len(idx) == 1:
            vidx = idx[0]
            if vidx == 0:
                V0 = pow(pow(V1, 2) - 2*a*S, 0.5)
                return V0
            elif vidx == 1:
                V1 = pow(pow(V0, 2) + 2*a*S, 0.5)
                return V1
            elif vidx == 2:
                a = (pow(V1, 2) - pow(V0, 2))/(2*S)
                return a
            elif vidx == 3:
                S = (pow(V1, 2) - pow(V0, 2))/(2*a)
                return S
            raise RuntimeError("LoL deu erro aki. parece que idx recebeu um valor invalido")
        else:
            print(len(idx))
            print("Error Mais de uma variavel esta sem valor.")
            quit()

    def __init__(self, V0=None, V1=None, a=None, S=None):
        pass

#  Refazer Estrutura    ******/////****** ******/////****** ******/////****** ******/////******



