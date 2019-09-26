# Resourses
from extensoes.Dependencies import *
from GetEnvPath import *


class Resourses:
    def __init__(self):
        self.DIR = G_PATH_CLASS.Recursos
        self.icon = self.DIR+"icon.png"
        self.logo = None
        self.background = {}
        self.images = {}

    def addImage(self, name, file):
        self.images[name] = CoreImage(self.DIR+file)

    def addBackground(self, name, file):
        self.background[name] = CoreImage(self.DIR+file)

    def addLogo(self, file):
        self.logo = CoreImage(self.DIR+file)



