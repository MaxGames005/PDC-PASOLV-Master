# Funcoes
from extensoes.Dependencies import *
from gscripts.Gmath.gmath_extensao import *
from gscripts.Gmath.gmath_funcao import *

ERRORS = {0: "Erro no nome da Função.",
          1: "Erro no Argumento da Função.",
          2: "Erro no Corpo da Função.",
          3: "Erro de Montagem do Obejto de Funçao.",
          4: "Erro de Montagem de Dados Crus"}


def dismember(vect):
    del vect


class Formula:

    def __init__(self, master):
        self.__master = master
        self.__Ftext = None
        self.__FFtext = None
        self.__Fname = None
        self.__Fargs = None
        self.__Fbody = None
        self.__Fobjt = None
        self.__proval = None
        self.raw = None
        self.log = True
        self.__Vbody = None
        self.__Vobj = None

    def ff(self):  # format function use to format function this is obvios enough
        function_string = None
        here = None

        try:
            here = 0
            self.__Fname = self.__FFtext[:self.__FFtext.find('(')].replace(' ', '')  # name ex: F of F(x,y)
            here = 1
            self.__Fargs = self.__FFtext[self.__FFtext.find('(')+1:self.__FFtext.find(')')].replace(' ', '')
            # args ex: x,y of F(x,y)
            here = 2
            self.__Fbody = self.__FFtext[self.__FFtext.find('=')+1:].replace(' ', '')
            # body ex: ln(x) - y of F(x,y) = ln(x) - y
            here = 3
            function_string = f"lambda {self.__Fargs}: {self.__Fbody}"  # lambda args: body
            here = 4
            self.raw = self.__FFtext, function_string
        except:
            QMessageBox.information(self.__master, "Error", f"{ERRORS[here]}")

        try:
            self.__Fobjt = eval(function_string)
            if self.log:
                print(f'proval: {self.__proval}, Fstring: {function_string}')
            try:
                self.__Fobjt(self.__proval)
            except:
                self.__Fobjt(*self.__proval)

        except:
            QMessageBox.information(self.__master, "Error", "Não foi Possivel Evaluar o Objeto de Função")
            self.__Fname = None
            self.__Fargs = None
            self.__Fbody = None
            self.__Fobjt = None

    def add(self, string):
        if self.isfunction_check(string):
            self.__Ftext = string
            self.__FFtext = self.ff_text(self.__Ftext)
            if self.log:
                print(f"log0: FFtext: {self.__FFtext}, Ftext: {self.__Ftext}")
            self.ff()
        else:
            QMessageBox.information(self.__master, "Error", "Isso Não é uma Função Valida")
            self.__Fname = None
            self.__Fargs = None
            self.__Fbody = None
            self.__Fobjt = None
            if self.log:
                print(f"log1: \nFFtext: {self.__FFtext}, \nFtext: {self.__Ftext}, \nFargs: {self.__Fargs}, \nFbody: {self.__Fbody}, \nFobjt: {self.__Fobjt}")

    def get(self):
        return self.__Fobjt, self.__Fname, self.__Fargs, self.__Fbody

    def ff_text(self, string):
        buffer = string.replace('e^', "E.v")
        buffer = buffer.replace('^', "**")
        try:
            self.__proval = '('+buffer[buffer.find(';')+1:]+')'
            buffer = buffer[:buffer.find(';')]
            self.__proval = eval(self.__proval)
            return buffer
        except:
            QMessageBox.information(self.__master, "Error", "Erro de Argumento de Prova Invalido")
        

    @staticmethod
    def isfunction_check(string):
        if string.find('=') < 0 or string.find('(') < 0 or string.find(')') < 0 or not string[:string.find('(')]:
            return False
        else:
            return True

    def varadd_andgetresult(self, arg_var, funsc):
        self.__Vbody = f'({arg_var})'
        try:
            try:
                self.__Vobj = eval(arg_var)
            except:
                QMessageBox.information(self.__master, "Error", "Não foi Possivel Evaular a Variavel")
            try:
                return funsc(self.__Vobj)
            except:
                QMessageBox.information(self.__master, "Error", "Math Error")
        except:
            try:
                self.__Vobj = eval(arg_var)
            except:
                QMessageBox.information(self.__master, "Error", "Não foi Possivel Evaular as Variaveis")
            try:
                return funsc(self.__Vobj)
            except:
                QMessageBox.information(self.__master, "Error", "Math Error")


"""
Formula Example:
F(x,y,z,w)= -ln(x) + e(x*z) + x^(e((x+y)/z)) - w + 30
"""

