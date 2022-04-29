import code
import enum
import os
from pathlib import *
import numpy as np
import sys
import colorama
colorama.init(autoreset=True)

# pycalc package
from pycalc.dna2 import *
from pycalc.n_base import *
from pycalc.units import *


# *Additional import
'''
There are some function that use the same name.
The problem is that it overwrite the previous function.
But I want it to use function without writing a module name
because it reduce my typing speed when I use this calculator.
So the solution is to make more important function
overwrite the less one.
'''
# Quite insignificant
from matplotlib.pyplot import *
from pandas import *
# Mild important
from pandas import *
# Very important
from random import *
from math import *
from statistics import *


# *Setting
np.set_printoptions(precision=3, suppress=True)


# *Rename function / Alternate name for function
f = factorial
หรม = gcd
ครน = lcm


#TODO: Still need more test
from pycalc.general import *


# *Save all locals and globals variable
variables = globals().copy()
variables.update(locals())


# *Start interactive console
if __name__ == '__main__':
    # Quick function access by argument
    if (len_argv := len(sys.argv)) > 1:
        match sys.argv[1]:
            case 'scalc':
                scalc()
    
    shell = code.InteractiveConsole(variables)
    shell.interact()
