from gscripts.Gmath.gmath_extensao import *
from gscripts.Classes.Classes import *

"""=====Type Keys"""
F = 'function'
arg = 'arg'
sep = 'sep'
body = 'body'
obj = 'obj'
DBG = 'debug'
Dct = 'dict'
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
	   Ex: EquatorInstance.add('f(x,y) = x**2 - ln(y)')  #adiciona uma função
	-get: busca valor
	-sim:    simboliza uma variavel
	






	|=============================================================================================================|
	"""
	
	def __init__(self):
		self.__excstring = ""
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
		if IsEquatorFunction(string_function):
			try:
				self.__cls_vars[F]['name'], self.__cls_vars[F][arg], \
				self.__cls_vars[F][sep], self.__cls_vars[F][body] = EquatorFunction(string_function)
			except:
				return "Invalid Syntax"
			self.update()
			self.arg_len()
			self.turn_function_object()
			self.add_function_dict()
		else:
			return "Invalid Syntax"
	
	def add_var(self, vname, value):
		try:
			self.__cls_vars[Dct][Var][vname] = eval(value)
			self.__excstring += f'{vname} = {eval(value)}\n'
			self.update()
		except:
			return "Invalid Syntax"
	
	def operate(self, f_key, args):
		try:
			if IsEquatorArg(self.transform_arg(args), self.__dictf[f_key][1]):
				return self.get_result(self.__aobj, self.__dictf[f_key][0])
			else:
				return "Invalid Syntax"
		except:
			return "Not Found " + self.transform_arg(args)
	
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
		self.__cls_vars[F][obj] = eval(f'lambda {self.format_arg()}: {self.__fbody}')
		self.update()
		
	def transform_arg(self, args):
		exec(self.__excstring)
		try:
			self.__cls_vars[arg][obj] = eval(f'({args})')
			self.update()
			return str(eval(args))
		except NameError:
			return NameError
		
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


Eqt = Equator()
print(Eqt.add('f(x,y)=ln(x)**2+y**2'))
print(Eqt.add('g(x,y)=ln(x)**2-y**2'))
print(Eqt.add('h(x,y)=ln(x)**2+y**0.5'))
print(Eqt.add_var('x', '1'))
print(Eqt.operate('f', '((12,2))'))
print(Eqt.operate('g', '((12,2))'))
print(Eqt.operate('h', '((x,2))'))


