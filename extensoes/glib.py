# glib
from extensoes.Dependencies import *
from extensoes.IntermedLib import *
from gscripts.Algebra.ALLgebra import *
from gscripts.Classes.Classes import *
from gscripts.Fisica.GFisica import *
from gscripts.Formato.Formatos import *
from gscripts.Gmath.gmath import *
from gscripts.MetodoNumerico.Metodos import *
from gscripts.Lista.Listas import *
from gscripts.Strings.String import *
from gscripts.Vetor.Vetores import *
from screen.Screens import *
from recursos.Resourses import *
from gdata.Data import *
from bin.AppPages.Pages import *
from bin.AppAssist.Assistente import *
from controle.Root import *
from controle.Constantes import *
from GetEnvPath import *
from interfaces.Interface import *


"""=============================\\ Localizadores de Modulos e Membros \\============================================="""


class GFind:
    def __init__(self):
        self.modules = {}
        self.names = []
        self.classes = {}
        self.definitions = {}
        self.GetMembersThisPath()
        self.GetModulesThisPath()

    def GetMembersThisPath(self):
        """
        Recebe os Membros do path OS
        :return: nada
        """
        for name, obj in getmembers(os.path):
            if ismodule(obj):
                self.modules[name] = obj
                self.names.append(name)
            elif isclass(obj):
                self.classes[name] = obj
                self.names.append(name)
            elif isfunction(obj):
                self.definitions[name] = obj
                self.names.append(name)

    def GetModulesThisPath(self):
        """
        Recebe os Membros do path OS
        :return: nada
        """
        self.modules["UKNW"] = getmodule(os.path)

    def GetInMemberWithTag(self, member, tag):
        """
        :param member: self.member type dict
        :param tag: KPage, TkPage, WxPage;
        :return: math tags list
        """
        buffer = []
        for k in member:
            if tag in k:
                buffer.append(member[k])
        return buffer


class GetInMod:
    def __init__(self):
        self.tags = {}
        self.routines = {}
        self.functions = {}
        self.vars = {}
        self.classes = {}
        self.__debug = False
        self.InitParam()
        pass

    def get_routines(self):
        for name, obj in getmembers(sys.modules[__name__]):
            if isroutine(obj):
                self.routines[name] = obj
        pass

    def get_functions(self):
        for name, obj in getmembers(sys.modules[__name__]):
            if isfunction(obj):
                self.functions[name] = obj
        pass

    def get_with_tag(self, tag):
        if tag:
            for name, obj in getmembers(sys.modules[__name__]):
                if tag in name:
                    self.tags[name] = obj
        pass

    def get_vars(self, list_var_s):
        ls = list_var_s
        for i in ls:
            self.vars[i] = 0
        return Vars
        pass

    def InitParam(self):
        self.get_functions()
        self.get_routines()
        self.get_with_tag()

    def debug_switch(self):
        self.debug = not self.debug
        if self.debug:
            self.PrintDict(self.functions)
            self.PrintDict(self.routines)
            self.PrintDict(self.get_with_tag)

    class PrintDict:
        def __init__(self, dicto):
            self.__dicto = dicto
            self.prt()

        @staticmethod
        def prt():
            for i in self.__dicto:
                print(i, self.__dicto[i])


class GLib:
    """
    Global Class Geral Library 
    Glib is All modules in one
    """

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = eval(name)()


"""===============================\\ Ferramentas de Exibição de Console \\ =========================================="""


class PrintDict:
    def __init__(self, Dict):
        for i in Dict:
            print(i, Dict[i])


class HELP:
    def __init__(self, sub=None):
        self.sub = sub

    def __getattr__(self, name):
        if not self.sub:
            print(eval(name+".__doc__"))
        else:
            print(eval(name+"."+self.sub+".__doc__"))
        return eval(name)


"""==================================\\ Ferramentas de Aplicação \\=================================================="""


BUTTON = "Button"
LABEL = "Label"
GRID = "GridLayout"
TEXT = "Text"
ENTRY = "Entry"
CANVAS = "Canvas"
EVENT = "Event"
BOXLAYOUT = "BoxLayout" 


"""==================================\\ Ferramentas de Condição \\=================================================="""


class Checklist:
    """
    args (dicionario, lista_de_chaves)
    Retorna Verdadeiro se todos os membros da lista de chaves estiverem no dicionario
    """
    def __init__(self, dicinario, lista_de_chaves):
        self.__dicinario = dicinario
        self.__keylist = lista_de_chaves
        self.__check()

    def __check(self):
        mat = []
        for key in self.__keylist:
            try:
                self.__dicinario[key]
                mat.append(key)
            except:
                pass
        return mat











