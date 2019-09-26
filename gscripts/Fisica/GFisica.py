# GFisica
# -*- coding: UTF-8 -*-
from gscripts.Fisica.Mecanica import *
from gscripts.Fisica.MecanicaDosSolidos import *


class PercaDeCargaLocalizada:
    def __new__(cls):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__()

        print("")
        labelstring = ["Dn: ", "Q: ", "Dh: ", "K: ", "Va: ", "Vb: ", "g: "]
        args = [[], [], [], [], [], [], []]
        for i in range(len(args)):
            try:
                args[i] = float(input(labelstring[i]))
            except:
                args[i] = None

        if args[0] != None:
            Dn = (pi*pow(args[0], 2))/4
        else:
            Dn = None
        Q = args[1]
        Dh = args[2]
        K = args[3]
        if Q != None and Dn != None:
            Va = Q/Dn
        else:
            Va = args[4]
            if Dn != None:
                Q = Va*Dn
        Vb = args[5]
        g = args[6]
        if Dh != None and K != None and Va != None and Vb != None and g == None:
            g = (K*pow(Va, 2)*Vb)/(2*Dh)
            print("\ng: ")
            return g
        elif Dh != None and K != None and Va != None and Vb == None and g != None:
            Vb = (2*g*Dh)/(K*pow(Va, 2))
            print("\nVb: ")
            return Vb
        elif Dh != None and K != None and Va == None and Vb != None and g != None:
            Va = pow((2*g*Dh)/(K*Vb), 0.5)
            print("\nVa: ")
            return Va
        elif Dh != None and K == None and Va != None and Vb != None and g != None:
            K = (2*g*Dh)/(K*pow(Va, 2))
            print("\nK: ")
            return K
        elif Dh == None and K != None and Va != None and Vb != None and g != None:
            Dh = (K*pow(Va, 2)*Vb)/(2*g)
            print("\nDh: ")
            return Dh
        else:
            print("Deu Ruim Ai da Uma olhada se voce deixou alguma informação sem colocar ou se voce preencheu tudo")

    def __init__(self):
        pass

#  Refazer Estrutura    ******/////****** ******/////****** ******/////****** ******/////******


class FisQ:
    def __init__(self, k, L, A, DT, DQ, Dt):
        pass

