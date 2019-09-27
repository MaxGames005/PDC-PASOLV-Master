from extensoes.Dependencies import *
from gscripts.Classes.Classes import *

"""=====Type Keys"""
F = 'function'
arg = 'arg'
sep = 'sep'
body = 'body'
obj = 'obj'
DBG = 'debug'
Dtc = 'dict'
Var = 'var'
Cb = 'callback'

class Equator:
    """Equator gera objetos atraves de string em formato de equação
    |======================|
    |        Param         |
    |==========================================================================================|
    |self.__fname            ->  function name <type 'string'>                                 |
    |self.__farg             ->  function argument <type 'string'>                             |
    |self.__fsep             ->  function separator <type 'string'>                            |
    |self.__fbody            ->  function body <type 'string'>                                 |
    |self.__fobj             ->  function object <type 'function object'>                      |
    |self.__vobj             ->  variable object <type undef" 'float', 'int', 'complex' ">     |
    |self.__vname            ->  variable name <type 'string'>                                 |
    |self.__alen             ->  argument length <type 'int'>                                  |
    |self.__aobj             ->  argument object <type 'object'>                               |
    |self.__debug            ->  debug <type 'bool'>                                           |
    |self.__dictf            ->  dict function <type 'dict'>                                   |
    |self.__dict_var         ->  dict variable <type 'dict'>                                   |
    |self.__dict_callback    ->  dict callback <type 'dict'>                                   |
    |==========================================================================================|



    |======================|
    |        Using         |
    |=============================================================================================================|
    Primeiro crie uma instancia de Equator() para armazenar suas funções, pois toda vez que equator for chamado
    ele ira zerar seus atributos apagando qualquer informação inserida.
        Ex: EquatorInstance = Equator()

    Comandos <<<

    -add: EquatorInstance.add('string_function')
       Ex: Equator().add('f(x,y) = x**2 - ln(y)')  #adiciona uma função
    -get: busca valor
    -sim:    simboliza uma variavel
    






    |=============================================================================================================|
    """
    def __init__(self):
        self.__fname = None         # function name <type 'string'>
        self.__farg = None          # function argument <type 'string'>
        self.__fsep = None          # function separator <type 'string'>
        self.__fbody = None         # function body <type 'string'>
        self.__fobj = None          # function object <type 'function object'>
        self.__vobj = None          # variable object <type undef" 'float', 'int', 'complex' ">
        self.__vname = None         # variable name <type 'string'>
        self.__alen = None          # argument length <type 'int'>
        self.__aobj = None          # argument object <type 'object'>
        self.__debug = False        # debug <type 'bool'>
        self.__dictf = {}           # dictionary function <type 'dict'>
        self.__dict_var = {}        # dictionary variable <type 'dict'>
        self.__dict_callback = {}   # dictionary callback <type 'dict'>

        self.__cls_vars = {F: {'name': self.__fname,  # #RefType
                               arg: self.__farg,
                               sep: self.__fsep,
                               body: self.__fbody,
                               obj: self.__fobj},

                           arg: {obj: self.__aobj,
                                'len': self.__alen},

                           Var: {'name': self.__vname, obj: self.__vobj},

                           DBG: self.__debug,

                           Dtc: {F: self.__dictf,
                                 Var: self.__dict_var,
                                 Cb: self.__dict_callback}}

        self.debug(self.__cls_vars)

    def debug(self, dict_arg):
        if self.__debug:
            print('**================================DEBUG================================**')
            for parent_key in dict_arg:
                print('||==================================================||')
                print(str(parent_key)+':', end='')
                for child_key in dict_arg[key]:
                    print(str(child_key)+':', dict_arg[parent_key][child_key], end='')
                print('\n||==================================================||')
            print('**================================DEBUG================================**')

    def log(self):
        self.__cls_vars[DBG] = not self.__cls_vars[DBG]

    def update(self):
        self.__fname = self.__cls_vars[F]['name']
        self.__farg = self.__cls_vars[F][arg]
        self.__fsep = self.__cls_vars[F][sep]
        self.__fbody = self.__cls_vars[F][body]
        self.__fobj = self.__cls_vars[F][obj]
        self.__vobj = self.__cls_vars[Var][obj]
        self.__vname = self.__cls_vars[Var]['name']
        self.__alen = self.__cls_vars[arg]['len']
        self.__aobj = self.__cls_vars[arg][obj]
        self.__debug = self.__cls_vars[DBG]
        self.__dictf = self.__cls_vars[Dtc][F]
        self.__dict_var = self.__cls_vars[Dtc][Var]
        self.__dict_callback = self.__cls_vars[Dtc][Cb]

    def add(self, string_function):
        if IsEquatorFunction(string_function):
            self.__cls_vars[F]['name'], self.__cls_vars[F][arg],\
                self.__cls_vars[F][sep], self.__cls_vars[F][body] = EquatorFunction(string_function)
        else:
            return

    def check_f_completion(self):
        if self.__cls_vars[F]['name'] and self.__cls_vars[F][arg] \
                and self.__cls_vars[F][sep] and self.__cls_vars[F][body]:
            return True
        else:
            return False

# print(Equator().__doc__)


