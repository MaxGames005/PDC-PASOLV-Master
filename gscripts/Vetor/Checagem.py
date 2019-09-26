"""Manipulador de listas"""


class IndexLim:  # delimita um valor maximo que pode ser obitido utilizado para correções de indice
    def __new__(cls, *args, **kwargs):
        instance = super(cls.__class__, cls).__new__(cls)
        instance.__init__(*args)
        if args[2] == None:
            if args[0] < args[1]:
                return args[0]
            elif args[0] >= args[1]:
                return args[1]
        else:
            if args[2] > args[0]:
                return args[2]
            elif args[0] < args[1] and args[0] >= args[2]:
                return args[0]
            elif args[0] >= args[1]:
                return args[1]

    def __init__(self, input_value, Max, Min=None):
        pass