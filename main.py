import code
import enum
from pathlib import *


# *Additional import
'''
There are some function that use the same name.
The problem is that it overwrite the previous function.
What I have seen is numpy and math module.
But I want it to use function without writing a module name
because it reduce my typing speed when I use this calculator.
So the solution is to make more important function
overwrite the less one.
'''
# Quite insignificant
from matplotlib.pyplot import *
from pandas import *
# Mild important
from numpy import *
from numpy.linalg import *
from pandas import *
arr_isclose = isclose       # Rename
# Very important
from random import *
from math import *


# *Setting
set_printoptions(precision=3, suppress=True)


# *Rename function / Alternate name for function
f = factorial


# *Additional variables
# Radian constant
RAD = pi / 180
# DNA and RNA
DNARNA = enum.Enum('DNA RNA', 'A G C')
A = DNARNA.A
G = DNARNA.G
C = DNARNA.C
DNA = enum.Enum('DNA', 'T')
T = DNA.T
RNA = enum.Enum('RNA', 'U')
U = RNA.U
del DNA, RNA, DNARNA
# Path
CWD = Path.cwd()


# *Additional function
# Trigonometry
def rada(x): return x * pi / 180        # Radian to Angle
def sina(x): return sin(rada(x))        # Sin of angle
def cosa(x): return cos(rada(x))        # Cos of angle
def tana(x): return tan(rada(x))        # Tan of angle
def csca(x): return arcsin(rada(x))     # Csc of angle
def seca(x): return arccos(rada(x))     # Sec of angle
def sota(x): return arctan(rada(x))     # Cot of angle
# Probability and etc.
def c(n, k): return f(n) / (f(k) * f(n - k))  # Choose
# Quick sum
def suml(*x): return sum(list(*x))        # Sum of List
def sumlm(*x): return suml(map(*x))     # Sum of List of Map
# Chemistry
# p = -log10
def p(x): return -log10(x)
# Chemical rate
def c_rate(concentration_start, concentration_stop, duration):
    return (concentration_start - concentration_stop) / duration


# *Special function
# Variable recorder
var_rec_list = []
# Record variable
def vrec(*v):
    global var_rec_list
    var_rec_list += v
# Recorded variable list print
def vrec_p():
    print(var_rec_list)
# Recorded variable list pop
def vrec_pop():
    var_rec_list.pop()
# Recorded variable list delete
def vrec_de(v):
    var_rec_list.remove(v)


# *Save all locals and globals variable
variables = globals().copy()
variables.update(locals())


# *Start interactive console
if __name__ == '__main__':
    shell = code.InteractiveConsole(variables)
    shell.interact()
