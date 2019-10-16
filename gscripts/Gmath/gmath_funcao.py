from gscripts.Gmath.gmath_extensao import *
from gscripts.Classes.Classes import *


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
       Ex: EquatorInstance.add('f(x,y) = x**2 - ln(y)')  #adiciona uma função
    -get: busca valor
    -sim:    simboliza uma variavel







    |=============================================================================================================|
    """

    def __init__(self):
        self.__last_var = None
        self.__last = None
        self.__transform_mod = False
        self.__fshow = {}
        self.__excstring = {}
        self.__fname = None  # function name <type 'string'>
        self.__farg = None  # function argument <type 'string'>
        self.__fsep = None  # function separator <type 'string'>
        self.__fbody = None  # function body <type 'string'>
        self.__fobj = None  # function object <type 'function object'>
        self.__vobj = None  # variable object <type undef" 'float', 'int', 'complex' ">
        self.__vname = None  # variable name <type 'string'>
        self.__abody = None
        self.__alen = None  # argument length <type 'int'>
        self.__aobj = None  # argument object <type 'object'>
        self.__debug = False  # debug <type 'bool'>
        self.__dictf = {}  # dictionary function <type 'dict'>
        self.__dict_var = {}  # dictionary variable <type 'dict'>
        self.__dict_callback = {}  # dictionary callback <type 'dict'>

        self.__cls_vars = {F: {'name': self.__fname,  # #RefType
                               arg: self.__farg,
                               sep: self.__fsep,
                               body: self.__fbody,
                               obj: self.__fobj},

                           arg: {obj: self.__aobj,
                                 'len': self.__alen,
                                 body: self.__fbody},

                           Var: {'name': self.__vname, obj: self.__vobj},

                           DBG: self.__debug,

                           Dct: {F: self.__dictf,
                                 Var: self.__dict_var,
                                 Cb: self.__dict_callback}}

        self.debug(self.__cls_vars)

    def debug(self, dict_arg):
        if self.__debug:
            print('**================================DEBUG================================**')
            for parent_key in dict_arg:
                print('||==================================================||')
                print(str(parent_key) + ':', end='')
                for child_key in dict_arg[parent_key]:
                    print(str(child_key) + ':', dict_arg[parent_key][child_key], end='')
                print('\n||==================================================||')
            print('**================================DEBUG================================**')

    def log_switch(self):
        self.__cls_vars[DBG] = not self.__cls_vars[DBG]

    def update(self):
        self.__fname = self.__cls_vars[F]['name']
        self.__farg = self.__cls_vars[F][arg]
        self.__fsep = self.__cls_vars[F][sep]
        self.__fbody = self.__cls_vars[F][body]
        self.__fobj = self.__cls_vars[F][obj]
        self.__vobj = self.__cls_vars[Var][obj]
        self.__vname = self.__cls_vars[Var]['name']
        self.__abody = self.__cls_vars[arg][body]
        self.__alen = self.__cls_vars[arg]['len']
        self.__aobj = self.__cls_vars[arg][obj]
        self.__debug = self.__cls_vars[DBG]
        self.__dictf = self.__cls_vars[Dct][F]
        self.__dict_var = self.__cls_vars[Dct][Var]
        self.__dict_callback = self.__cls_vars[Dct][Cb]
        self.debug(self.__cls_vars)

    def add(self, string_function):
        """adiciona os sigmentos de função"""
        tentativa = TryDo(EquatorFunction, string_function)
        nome = None
        if tentativa:
            nome = tentativa[0]
        else:
            return "Invalid Syntax"
        if IsEquatorFunction(string_function) and nome not in self.__dict_var:
            try:
                self.__cls_vars[F]['name'], self.__cls_vars[F][arg], \
                self.__cls_vars[F][sep], self.__cls_vars[F][body] = EquatorFunction(string_function)
                self.__fshow[self.__cls_vars[F]['name']] = ''.join(EquatorFunction(string_function))
                self.__last = self.__fshow[self.__cls_vars[F]['name']]
            except:
                return "Invalid Syntax"
            self.update()
            self.arg_len()
            if self.turn_function_object():
                return self.turn_function_object()
            self.add_function_dict()
        else:
            if not nome or not IsEquatorFunction(string_function):
                return "Invalid Syntax"
            else:
                return 'Name Is Already Occupied'

    def remove_function(self, fname):
        if fname in self.__fshow:
            self.__cls_vars[Dct][F].pop(fname)
            self.__fshow.pop(fname)
            self.update()

    @staticmethod
    def callback(event):
        print(event)

    def show_function(self, fname):
        if fname in self.__fshow:
            return self.__fshow[fname]
        else:
            return "Not Found: "+fname

    def last_added(self):
        return self.__fname, self.__last

    def match_chars(self, string1, string2):
        if not self.has_banned_word(string1):
            match = None
            for char in string1:
                if char in string2:
                    match = True
                else:
                    match = False
                    break
            return match
        else:
            return self.has_banned_word(string1)

    def has_banned_word(self, string):
        for banw in baned_words:
            if banw in string:
                return banw
        return False

    def add_var(self, string):
        vname , value = self.add_var_format(string)
        if not isinstance(self.match_chars(vname, restrict), str) and self.match_chars(vname, restrict)\
                and vname not in self.__dictf and not self.has_banned_word(value):
            try:
                last = None
                try:
                    for variable in self.__excstring:
                        last = variable, self.__excstring
                        exec(self.__excstring[variable])
                except:
                    return "Unknown Error: " + str(last)
                self.__cls_vars[Dct][Var][vname] = eval(value)
                self.__excstring[vname] = f'{vname} = {eval(value)}\n'
                self.__last_var = vname, eval(value), f'{vname} = {eval(value)}'
                self.update()
            except:
                return "Invalid Value"
        else:
            if vname in self.__dictf:
                return 'Name Is Already Occupied'
            elif isinstance(self.match_chars(vname, restrict), str):
                return "Banned Word: " + self.match_chars(vname, restrict)
            elif self.has_banned_word(value):
                return "Banned Word: " + self.has_banned_word(value)
            else:
                return "Invalid Characters:" + self.restrict_chars(vname)

    def get_var_dict(self):
        return self.__dict_var

    def get_function_dict(self):
        return self.__dictf

    def last_var(self):
        return self.__last_var

    @staticmethod
    def add_var_format(string):
        vname = UntilFind(string, '=').replace(' ', '')
        value = AfterFind(string, '=', 1).replace(' ', '')
        return vname, value

    def restrict_chars(self, string):
        buf = ""
        for char in string:
            if char not in restrict and char not in buf:
                buf += ' '+char
        return buf

    def operate(self, f_key, args):
        try:
            if IsEquatorArg(self.transform_arg(args), self.__dictf[f_key][1]):
                return self.get_result(self.__aobj, self.__dictf[f_key][0])
            else:
                return "Invalid Syntax"
        except:
            return "Invalid Arg: " + args

    def add_function_dict(self):
        if self.function_is_completed():
            self.__cls_vars[Dct][F][self.__fname] = self.__fobj, self.__alen
            self.update()

    def get_fdict(self):
        buf = {}
        for key in self.__dictf:
            buf[key] = self.__dictf[key][0]
        return buf

    def function_is_completed(self):
        if self.__cls_vars[F]['name'] and self.__cls_vars[F][arg] \
                and self.__cls_vars[F][sep] and self.__cls_vars[F][body]:
            return True
        else:
            return False

    def turn_function_object(self):
        try:
            self.__cls_vars[F][obj] = eval(f'lambda {self.format_arg()}: {self.__fbody}')
            self.__excstring[self.__fname] = f'{self.__fname} = lambda {self.format_arg()}: {self.__fbody}\n'
            self.update()
        except:
            return "Erro No Corpo Da Função: "+str(self.__fbody)

    def execute(self):
        last = None
        try:
            for variable in self.__excstring:
                last = variable, self.__excstring
                exec(self.__excstring[variable])
            return None
        except:
            return "Unknown Error: " + str(last)

    def transform_arg(self, args):
        last = None
        try:
            for variable in self.__excstring:
                last = variable, self.__excstring
                exec(self.__excstring[variable])
        except:
            return "Unknown Error: " + str(last)

        try:
            self.__cls_vars[arg][obj] = eval(f'({args})')
            self.update()
            return str(eval(args))
        except:
            return "Value Error"

    def format_arg(self):
        return self.__farg.replace('(', '').replace(')', '')

    def arg_len(self):
        string_argv = self.format_arg().split(',')
        if isinstance(string_argv, tuple) or isinstance(string_argv, list):
            string_argv = ClearNones(string_argv)
            self.__cls_vars[arg]['len'] = len(string_argv)
        elif isinstance(string_argv, str):
            self.__cls_vars[arg]['len'] = 1
        self.update()

    @staticmethod
    def get_result(args, funf):
        """Tenta calcular a função pela passagem dos objetos {argumentos ,função}"""
        try:
            try:
                return funf(*args)
            except:
                return funf(args)
        except:
            return "Math Error"

    def remove(self, name):
        if name not in self.__dict_var and name not in self.__dictf:
            return "Not Found: " + name
        elif name in self.__dictf:
            self.__dictf.pop(name)
            self.__excstring.pop(name)
        elif name in self.__dict_var:
            self.__dict_var.pop(name)
            self.__excstring.pop(name)
        else:
            return 'Erro Cabuloso!!'



Eqt = Equator()




