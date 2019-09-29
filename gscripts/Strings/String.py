# String

""" Manipulação de Strings """


class UntilFind:
    """UntilFind ferramenta de manipulação de string busca o valor de uma string até o primeiro encontro do caractere
    especificado.

    |USO|: UntilFind('string_com_!_proximo_ao_centro', '!') ; |SAIDA|:'string_com_'
    """
    def __init__(self, string, char, stop=0):
        self.__string = string
        self.__char = char
        self.__stop = stop
        self.__ufstring = self.__ufind()

    def __new__(cls, string, char, stop=0):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(string, char, stop)
        return inst.__ufstring

    def __ufind(self):
        return self.__string[:self.__string.find(self.__char)+self.__stop]


class AfterFind:
    def __init__(self, string, char, start=0):
        self.__string = string
        self.__char = char
        self.__start = start
        self.__afstring = self.__affind()

    def __new__(cls, string, char, start=0):
        inst = super(AfterFind, cls).__new__(cls)
        inst.__init__(string, char, start)
        return inst.__afstring

    def __affind(self):
        return self.__string[self.__string.find(self.__char)+self.__start:]


class String:
    def __init__(self, string):
        self.string = string

    def clear_voids(self):
        """Armazena todos os não vazios"""
        buuf = []
        for i in self.string:
            if i != None and i != "":
                buuf.append(i)
        return buuf

    def split_par(self):
        aux = []
        for i in range(len(self.string)):
            pass

    def revs(self):
        return self.string[-1:-len(self.string) - 1:-1]






