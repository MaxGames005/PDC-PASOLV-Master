from math import *
import numpy as np


class Transformation:
	def __init__(self):
		self.__











"""
||x|2|1|     |
||4|0|1| - yI| = 0
||3|5|2|     |

||x-y|2   |1  ||
||4  |0-y |1  || = 0
||3  |5   |2-y||

(x-y)(2-y)(0-y) + 6 + 20 - 3(0-y) -8(2-y) -5(x-y) = 0
(x-y)(2-y)(0-y) + 26 - 3y - 16 +8y -5x + 5y       = 0
(x-y)(2-y)(0-y) + 10 + 10y -5x 					  = 0
(x-y)(2-y)(0-y) + 10(1+y) - 5x  				  = 0
(2x - xy -2y + y²)(0-y) + 10 + 10y -5x			  = 0
-2xy + xy² + 2y² - y³ + 10y + 10 -5x 			  = 0
y(-2x + xy + 2y - y² + 10) + 10 -5x				  = 0

(-2+5)(2+5)(0+5) + 6 + 20 - 3(0+5) -8(2+5) -5(-2+5) = 3*7*5 + 6 + 20 - 15 - 56 - 15 = 105 + 6 + 20 - 15 - 56 - 15 = 55


(y-x) + 2 + 1 = 0
4 + (y-0) + 1 = 0
3 + 5 + (y-2) = 0

(y-x) = y = x -3
(y-0) = y = -5
(y-2) = y = 7 

x = -2
x = 10

-y = -5, y = 5

2-5=-8

"""


y = 0j
"""0, -2"""
y1 = 0
y2 = 0
y3 = 0
x = 2

print((2-y)*(2-y)*(0-y) + 26 - 3*(0-y) -8*(2-y) -5*(2-y))





