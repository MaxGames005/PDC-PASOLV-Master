# String

""" Manipulação de Strings """


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






