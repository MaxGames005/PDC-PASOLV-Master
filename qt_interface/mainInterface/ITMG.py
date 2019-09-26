from os import *
from io import *
from time import *


class Manager:
	def __init__(self):
		self.__authentiqued = False
		self.__filename = str(input("filename.ui: "))
		if not self.__filename:
			self.__filename = "PDC Pasolv Master.ui"
		self.__file = getcwd()
		print('filename.ui: '+self.__filename+' at: '+self.__file)
		self.FormatPath()
		self.__command = f'pyuic5 "{self.__file}" -o {f""" "{self.__filename[:-3]}.py" """}'
		print(self.__command) 
		print(self.__file)
		self.Make()

	def FormatPath(self):
		self.__file = list(self.__file)
		self.__file.reverse()
		self.__file = "".join(self.__file)["".join(self.__file).find('\\')+1:]
		self.__file = list(self.__file)
		self.__file.reverse()
		self.__file = "".join(self.__file)+"\\"
		self.__file += self.__filename

	def Make(self):
		system(self.__command)


Inst = Manager()