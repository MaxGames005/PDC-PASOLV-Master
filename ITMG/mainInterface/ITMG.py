from os import *
from io import *
from time import *

from GetEnvPath import *


Header = """'''
Interface Grafica do Pasolv Versao Master
'''


from Extensoes.Dependencies import *
from GetEnvPath import *"""

version = "5"
uic = "pyuic"+version 



class Tags:
	def __getattr__(self, item):
		if item == 'tags':
			self.__dict__[item] = []
			file = open(GPC.MainInterface+'tags.txt', 'r')
			content = file.readlines()
			aux = ""
			for line in content:
				for ch in line:
					if ch != ':':
						aux += ch
					else:
						aux = '"'+aux.replace(" ", "")+'"'
						self.__dict__[item].append([aux.replace(chr(13),""), (line[line.find(':')+1:].replace(" ", "")).rstrip()])
						aux = ""
						break
			return self.__dict__[item]

Tag = Tags()


class Manager:
	"""Manager
	call filename ui
	return filename py
	convertion with pyuic5
	"""
	def __init__(self):
		self.__FormatedPyFile = "Interface.py"
		self.__File = None
		self.__Content = None
		self.__ContentBuffer = []
		self.__authentiqued = False
		self.__filename = str(input("filename.ui: "))  # filename.ui
		if not self.__filename:
			self.__filename = "PDC Pasolv Master.ui"
		self.__file = GPC.ITMG
		self.__filepath = GPC.ITMG
		print("File Path: "+self.__file)
		print('filename.ui: '+self.__filename+' at: '+self.__file)
		self.FormatPath()
		self.__pyfilename = self.__filename[:-3] + '.py'  # filename.py
		self.__command = f'{uic} "{self.__file}" -o {f""" "{self.__filepath+self.__pyfilename}" """}'
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
		self.__file += self.__filename  # Path\\filename.ui

	def Make(self):
		system(self.__command)
		self.FormatFile()

	def FormatFile(self):
		self.__File = open(self.__filepath+self.__pyfilename, 'r')
		self.__Content = self.__File.read()
		self.FormatContent()
		self.__File.close()
		self.CEPyFile()
		self.__File = open(GPC.Interfaces+self.__FormatedPyFile, "w")
		self.__File.write(self.__Content)
		self.__File.close()

	def CEPyFile(self):  # create a empty .py file in a especifiqued directory
		newfile = open(GPC.Interfaces+self.__FormatedPyFile, "a")
		newfile.close()
		newfile = open(GPC.Interfaces+self.__FormatedPyFile, "w")
		newfile.close()

	def FormatContent(self):
		self.__ContentBuffer.append(self.__Content[:self.__Content.find('QtWidgets')+9])
		self.__Content = self.__Content.replace(self.__ContentBuffer[0], Header)
		for tag, content in Tag.tags:
			self.__Content = self.__Content.replace(tag, content)