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

        string_before_sep = UntilFind(self.__eqf, '=')
        if not string_before_sep or self.__eqf.find('=') == -1:
            return False
        self.__eqf = self.__eqf.replace(string_before_sep, '')
        self.__split_eqf.append(UntilFind(string_before_sep, '('))
        self.__split_eqf.append(UntilFind(string_before_sep, ')', 1).replace(UntilFind(string_before_sep, '('), ''))
        self.__split_eqf.append(UntilFind(self.__eqf, '=', 1))
        self.__eqf = self.__eqf.replace(self.__split_eqf[-1], '')
        if not self.__eqf:
            return False
        self.__split_eqf.append(self.__eqf)
        return True


class IsEquatorArg:
    """IsEquatorArg uma ferramenta de controle verifica se uma string e uma string no formato EquatorArg
    |USO|: IsEquatorArg('x,y,z', 'F(x,y,z)') ; |SAIDA|: True --> F(x,y,z)
    |USO|: IsEquatorArg('x,y,z', 'F(x,y)')  ; |SAIDA|: False --> F(x,y)
    """
    def __init__(self, arg_body, function_arg_length):
        self.__conclusion = None
        try:
            if isinstance(eval(arg_body), int) or isinstance(eval(arg_body), float):
                if function_arg_length == 1:
                    self.__conclusion = True
                else:
                    self.__conclusion = False
            elif isinstance(eval(arg_body), list) or isinstance(eval(arg_body), tuple):
                if function_arg_length == len(eval(arg_body)):
                    self.__conclusion = True
                else:
                    self.__conclusion = False
            else:
                self.__conclusion = False
        except:
            self.__conclusion = False

    def __new__(cls, arg_body, function_arg_length):
        inst = super(IsEquatorArg, cls).__new__(cls)
        inst.__init__(arg_body, function_arg_length)
        return inst.__conclusion


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
        string_before_sep = UntilFind(self.__eqf, '=')
        if not string_before_sep:
            return False
        self.__eqf = self.__eqf.replace(string_before_sep, '')
        self.__split_eqf.append(UntilFind(string_before_sep, '('))
        self.__split_eqf.append(UntilFind(string_before_sep, ')', 1).replace(UntilFind(string_before_sep, '('), ''))
        self.__split_eqf.append(UntilFind(self.__eqf, '=', 1))
        self.__eqf = self.__eqf.replace(self.__split_eqf[-1], '')
        if not self.__eqf:
            return False
        self.__split_eqf.append(self.__eqf)
        return self.__split_eqf


class ClearNones:
    """Como o nome diz mas somente retorna listas ou dicionarios"""
    def __init__(self, arg):
        if isinstance(arg, tuple) or isinstance(arg, list):
            self.__bufer = []
            for i in arg:
                if i:
                    self.__bufer.append(i)
        elif isinstance(arg, dict):
            self.__bufer = {}
            for key in arg:
                if arg[key]:
                    self.__bufer[key] = arg[key]
        else:
            self.__bufer = None

    def __new__(cls, arg):
        inst = super(ClearNones, cls).__new__(cls)
        inst.__init__(arg)
        return inst.__bufer


class Redundancy:
    """Redundancy é uma classe de checagem de dois objetos de tipos similares, verifica o encontro de uma redundancia
    |USO|: Redundancy(list1,list2) ; |SAIDA|: True ou False depende se existe um termo redundante
    |NOT_BREAK_ERROR|: Different Types Can't be able to Have Redundancy |EVER|: False """
    def __init__(self, arg1, arg2):
        self.__arg1 = arg1
        self.__arg2 = arg2
        self.__conclusion = self.__verify()

    def __new__(cls, arg1, arg2):
        inst = super(Redundancy, cls).__new__(cls)
        inst.__init__(arg1, arg2)
        return inst.__conclusion

    def __verify(self):
        if isinstance(self.__arg1, type(self.__arg2)):
            if isinstance(self.__arg1, dict):
                for key in self.__arg1:
                    if key in self.__arg2:
                        return True
                return False
            elif isinstance(self.__arg1, list) or isinstance(self.__arg1, tuple):
                for item in self.__arg1:
                    if item in self.__arg2:
                        return True
                return False
            else:
                return False
        else:
            #print("Error Different Types Can't be Redundant")
            return False


class TryDo:
    def __init__(self, element, *args, **kwargs, ):
        self.__obj = element
        self.__args = args
        try:
            self.__callback = kwargs['callback']
        except:
            self.__callback = lambda ev: ev
        self.__return = self.__doatry()

    def __new__(cls, element, *args, **kwargs):
        inst = super(TryDo, cls).__new__(cls)
        inst.__init__(element, *args, **kwargs)
        return inst.__return

    def __doatry(self):
        try:
            return self.__obj(*self.__args)
        except Exception as excpt:
            self.__callback(excpt)
            return None







