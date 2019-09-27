# Classes
from gscripts.Strings.String import *


class IsNone:
    """IsNone feramenta de controle verifica se o objeto é vazio
    |USO|: IsNone('') ; |SAIDA|: True
    |USO|: IsNone(' ') ; |SAIDA|: False
    """
    def __init__(self, string):
        self.__conclusion = None
        if string:
            self.__conclusion = False
        else:
            self.__conclusion = True

    def __new__(cls, string):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(string)
        return inst.__conclusion


class BooleanInt:
    """BooleanInt ferramenta de conversão converte um argumento booleano em um inteiro correspondente
    |USO|: BooleanInt(True)  ; |SAIDA|: 1
    |USO|: BooleanInt(False) ; |SAIDA|: 0
    """
    def __init__(self, boolean_arg):
        self.__barg = boolean_arg
        self.__conclusion = None
        self.is_true()

    def __new__(cls, boolean_arg):
        inst = super(cls.__class__, cls).__new__(cls)
        inst.__init__(boolean_arg)
        return inst.__conclusion

    def is_true(self):
        if self.__barg:
            self.__conclusion = 1
        else:
            self.__conclusion = 0


class IsEquatorFunction:
    """IsEquatorFunction uma ferramenta de controle verifica se uma string e uma string no formato EquatorFunction
    |USO|: IsEquatorFunction('f(x,y) = ln(x) - exp(x**2)/x**4') ;   |SAIDA|: True
    |USO|: IsEquatorFunction('f = ln(x) - exp(x**2)/x**4')      ;   |SAIDA|: False
    |USO|: IsEquatorFunction('f(x,y) ln(x) - exp(x**2)/x**4')   ;   |SAIDA|: False
    |USO|: IsEquatorFunction('f(x,y) =')                        ;   |SAIDA|: False
    |USO|: IsEquatorFunction('f')                               ;   |SAIDA|: False
    """
    def __init__(self, string_eqfunction):
        self.__eqf = string_eqfunction.replace(' ', '')
        self.__split_eqf = []
        self.__conclusion = self.verification()

    def __new__(cls, string_eqfunction):
        inst = super(IsEquatorFunction, cls).__new__(cls)
        inst.__init__(string_eqfunction)
        return inst.__conclusion

    def verification(self):
        verif = 0
        index = 0

        self.__split_eqf.append(UntilFind(self.__eqf, '('))
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index]))
        index += 1

        self.__split_eqf.append(UntilFind(self.__eqf, ')', 1))
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index].replace('(', '').replace(')', '')))
        index += 1

        self.__split_eqf.append(UntilFind(self.__eqf, '=', 1))
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index]))
        index += 1

        self.__split_eqf.append(self.__eqf)
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index]))

        if self.__eqf:
            return False, None
        elif verif == 4:
            return True, self.__split_eqf
        else:
            return False, None


class EquatorFunction:
    """EquatorFunction uma ferramenta de conversão de string no formato EquatorFunction para lista
    |USO|: EquatorFunction('f(x,y) = ln(x) - exp(x**2)/x**4') ;   |SAIDA|: ['f','(x,y)','=','ln(x)-exp(x**2)/x**4']
    """
    def __init__(self, string_eqfunction):
        self.__eqf = string_eqfunction.replace(' ', '')
        self.__split_eqf = []
        self.__conclusion = self.verification()

    def __new__(cls, string_eqfunction):
        inst = super(EquatorFunction, cls).__new__(cls)
        inst.__init__(string_eqfunction)
        return inst.__conclusion

    def verification(self):
        verif = 0
        index = 0

        self.__split_eqf.append(UntilFind(self.__eqf, '('))
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index]))
        index += 1

        self.__split_eqf.append(UntilFind(self.__eqf, ')', 1))
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index].replace('(', '').replace(')', '')))
        index += 1

        self.__split_eqf.append(UntilFind(self.__eqf, '=', 1))
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index]))
        index += 1

        self.__split_eqf.append(self.__eqf)
        self.__eqf = self.__eqf.replace(self.__split_eqf[index], '')

        verif += BooleanInt(not IsNone(self.__split_eqf[index]))

        if self.__eqf:
            return None
        elif verif == 4:
            return self.__split_eqf
        else:
            return None






