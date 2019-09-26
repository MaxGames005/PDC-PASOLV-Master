from GetEnvPath import *

GLOBAL_DEPENDENCIES = {}
CONFIG_LIST = {"QT5": 0, "MAYAVI":1, "MATH":2, "MATPLOTLIB":3, "VTK":4, "GTK":5, "OPENGL":6, "TOOLS":7}


default_config = """QT5: True
MATPLOTLIB: True
TOOLS: True
MAYAVI: True
OPENGL: True
MATH: True
KIVY: False"""


class SetConfig:
    def __init__(self):
        global GLOBAL_DEPENDENCIES
        self.__cfgfile = None
        self.log = False

        try:
            self.__cfgfile = open(GPC.local + "config.txt", 'r')
        except:
            self.__cfgfile = open(GPC.local + "config.txt", "a")
            self.__cfgfile.close()
            self.__cfgfile = open(GPC.local + "config.txt", "w")
            self.__cfgfile.close()
            self.__cfgfile = open(GPC.local + "config.txt", "r")
        self.__cfg = self.__cfgfile.readlines()
        self.__enableds = self.__formatfile()
        for key, state in self.__enableds:
            GLOBAL_DEPENDENCIES[key] = state

    def __formatfile(self):
        cfg = self.__cfg
        buff = []
        for line in cfg:
            if self.log:
                print(line)
            buff.append([line[:line.find(':')].replace(" ", ""),
                         eval(line[line.find(':')+1:].replace(" ", ""))])
        return buff


SetConfig()








