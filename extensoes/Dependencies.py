from config import *
"""========================== Mathematican =============================="""
if GLOBAL_DEPENDENCIES["MATH"]:
	from math import *
	import numpy as np
	import scipy as sci
	from numpy import random
	import random
	from simpy import *
	import sympy
	import galgebra
	import chempy
	import lcapy
	import optlang
	import pyneqsys
	import pyodesys
	import sagemath
	import fdiff
	import spyder
# Last Change Here __+__
"""======================================================================"""

"""======================== Tools ============================="""
if GLOBAL_DEPENDENCIES["TOOLS"]:
	import sys
	import inspect
	from inspect import *
	from os import *
	from time import *
	from io import *
	from six import *
	import latex
	import socket
"""============================================================"""

"""======================== MatPlotLib ============================="""
#if GLOBAL_DEPENDENCIES["MATPLOTLIB"]:
try:
	from matplotlib import *
	from matplotlib.pyplot import *
	from matplotlib.backends.backend_tkagg import *
	from matplotlib.figure import *
	from matplotlib._pylab_helpers import *
	from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
	if is_pyqt5():
		from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
	else:
		from matplotlib.backends.backend_qt4agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
	from matplotlib.figure import *
	import matplotlib as mp
	import matplotlib.pyplot as mpl
except:
	pass
"""=========================================================="""

"""======================== OpenGL ============================="""
if GLOBAL_DEPENDENCIES["OPENGL"]:
	from OpenGL import *
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GLUT import *
"""=========================================================="""

"""======================== Kivy ============================="""
if GLOBAL_DEPENDENCIES["KIVY"]:
	import kivy as kv
	from kivy.app import *
	from kivy.app import App
	from kivy.uix import *
	from kivy.uix.label import *
	from kivy.uix.widget import *
	from kivy.uix.boxlayout import *
	from kivy.uix.button import Button
	from kivy.uix.gridlayout import GridLayout
	from kivy.uix.label import Label
	from kivy.uix.textinput import TextInput
	from kivy.uix.pagelayout import *
	from kivy.uix.image import Image
	from kivy.graphics import *
	from kivy.properties import ObjectProperty
	from kivy.lang import Builder
	from kivy.core.image import Image as CoreImage
	from kivy.config import Config
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.widget import Widget
	from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
	from kivy.properties import NumericProperty
	from kivy.properties import ListProperty
	kv.require('1.11.1')
"""=========================================================="""

"""======================== QT5 ============================="""
if GLOBAL_DEPENDENCIES["QT5"]:
	pass
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
"""=========================================================="""

"""========================== Mayavi =========================="""
if GLOBAL_DEPENDENCIES["MAYAVI"]:
	import mayavi
	from mayavi import *
"""============================================================"""

"""======================Colored Debug========================="""
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored


def alert(string):
	init()
	print(colored(string, 'red'))


"""============================================================"""

"""===========================Global Naming================================="""
OBJECT = "GObject"

"""=====Type Keys===="""
F = 'function'
arg = 'arg'
sep = 'sep'
body = 'body'
obj = 'obj'
DBG = 'debug'
Dct = 'dict'
Var = 'var'
Cb = 'callback'
restrict = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_,()"
baned_words = ['system', 'debug', 'print', 'import', 'from']

"""========================================================================="""



