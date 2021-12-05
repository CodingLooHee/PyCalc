import code
import enum
import os
from pathlib import *
import numpy as np


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


# *Setting
np.set_printoptions(precision=3, suppress=True)


# *Rename function / Alternate name for function
f = factorial
หรม = gcd
ครน = lcm


# *Additional variables
# Radian constant
RAD = pi / 180
# DNA and RNA
class N_BASE(enum.Enum):
    A = enum.auto()
    G = enum.auto()
    T = enum.auto()
    C = enum.auto()
    U = enum.auto()
# Path
CWD = Path.cwd()
# Unit
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deca = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24
# Physic
ke = 9e9        # K constant (electric)
qe = -1.6e-19   # Electron charge (coulomb)
qp = 1.6e-19    # Proton charge (coulomb)


# *Additional function
# Trigonometry
def rada(x): return x * pi / 180        # Radian to Angle
def sina(x): return sin(rada(x))        # Sin of angle
def cosa(x): return cos(rada(x))        # Cos of angle
def tana(x): return tan(rada(x))        # Tan of angle
def csca(x): return 1/sina(x)           # Csc of angle
def seca(x): return 1/cosa(x)           # Sec of angle
def sota(x): return 1/tana(x)           # Cot of angle
# Probability and etc.
def c(n, k): return f(n) / (f(k) * f(n - k))  # Choose
# Quick map convertion
def lm(*x): return list(map(*x))        # List of Map
def sm(*x): return set(map(*x))         # Set of Map
# Quick sum
def suml(*x): return sum(list(*x))      # Sum of List
def sumlm(*x): return suml(map(*x))     # Sum of List of Map
# Chemistry
# p = -log10
def p(x): return -log10(x)
# Chemical rate
def c_rate(concentration_start, concentration_stop, duration):
    return (concentration_start - concentration_stop) / duration
def root(x):
    return x**(1/2)
# Distance
def dis2(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return (dx**2 + dy**2)**(1/2)
def dis3(x1, y1, z1, x2, y2, z2):
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return (dx**2 + dy**2 + dz**2)**(1/2)


# *Additional class
# DNA #TODO: continue this feature
class DNA:
    def __init__(self, init_dna: str='') -> None:
        # Turn list into dna
        self.dna_template = self._dna2str(init_dna)
        
        # Getting non template dna
        self.dna_non_template = self._get_dna_oppose(self.dna_template)
    
    def __str__(self) -> str:
        return f'{self.template}'
        
    '''
    Please note that everytime something make change to the DNA sequence
    Non-template DNA must be changed oppose to template DNA and vice versa
    '''

    @property
    def template(self):                     # Get DNA in string format
        str_dna = ''
        for each_base in self.dna_template:
            str_dna += self._base2char(each_base)
        return str_dna
    
    @property
    def non_template(self):                 # Get non template DNA with string format
        str_dna = ''
        for each_base in self.dna_non_template:
            str_dna += self._base2char(each_base)
        return str_dna
    

    @template.setter
    def template(self, new_dna: str):       # Set DNA with string format
        self.dna_template = self._dna2str(new_dna)
        self.dna_non_template = self._get_dna_oppose(self.dna_template)
    
    @non_template.setter
    def non_template(self, new_dna:str):    # Set not template DNA with string format
        self.dna_non_template = self._dna2str(new_dna)
        self.dna_template = self._get_dna_oppose(self.dna_non_template)


    # Utility zone

    @staticmethod
    def _dna2str(str_dna: str):
        # Check if init_dna is string
        if type(str_dna) is not str:
            raise TypeError('This is not string')
        
        dna_template: list[N_BASE] = []
        # Turn list into dna
        for each_base in str_dna:
            match each_base:
                case 'A' | 'a':
                    dna_template.append(N_BASE.A)
                case 'G' | 'g':
                    dna_template.append(N_BASE.G)
                case 'T' | 't':
                    dna_template.append(N_BASE.T)
                case 'C' | 'c':
                    dna_template.append(N_BASE.C)
                case _:
                    raise ValueError('Only A G T C can be put')
        return dna_template
    
    @staticmethod
    def _get_dna_oppose(str_dna: list[N_BASE]):
        # Getting non template dna
        dna_non_template: list[N_BASE] = []
        for each_base in str_dna:
            match each_base:
                case N_BASE.A:
                    dna_non_template.append(N_BASE.T)
                case N_BASE.T:
                    dna_non_template.append(N_BASE.A)
                case N_BASE.G:
                    dna_non_template.append(N_BASE.C)
                case N_BASE.C:
                    dna_non_template.append(N_BASE.G)
        return dna_non_template
    
    @staticmethod
    def _base2char(base_single: N_BASE):
        match base_single:
            case N_BASE.A:
                return 'A'
            case N_BASE.G:
                return 'G'
            case N_BASE.T:
                return 'T'
            case N_BASE.C:
                return 'C'
            case _:
                raise ValueError('Not an N_BASE')



# *Special function
# CMD
def cmd(x): os.system(x)
# Clear
def cls(): cmd('cls')
# Score calculator
def scalc(countmode: str='wrong'):
    print('Enter a max score for the test')
    max_score = int(input('Max score: '))
    match countmode:
        case 'wrong' | 0:
            print('Each character represent a zero mark.')
            wrong_character = input('Enter character: ')
            wrong_score = len(wrong_character)
            score = max_score - wrong_score
        case 'right'| 1:
            print('Each character represent 1 mark.')
            correct_character = input('Enter character: ')
            score = len(correct_character)
        case _:
            raise TypeError('Not support')

    score_percentage = score*100/max_score

    print(f'Score: {score}/{max_score}')
    print(f'Percent: {score_percentage:.2f}%')


# *Save all locals and globals variable
variables = globals().copy()
variables.update(locals())


# *Start interactive console
if __name__ == '__main__':
    shell = code.InteractiveConsole(variables)
    shell.interact()
