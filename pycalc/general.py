from math import pi, sin, cos, tan, log10, log, e
from math import factorial as f
from pathlib import Path
import os
import colorama


# *Additional variables
# Radian constant
RAD = pi / 180
# Path
CWD = Path.cwd()
# Physic
ke = 9e9        # K constant (electric)
qe = -1.6e-19   # Electron charge (coulomb)
qp = 1.6e-19    # Proton charge (coulomb)
G = 6.67e-11    # Gravity constant (m^3/(kg.s^2))


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
# List accumulator
def acc(x):
    sum_value_accumulate = []
    sum_value = 0
    for value in x:
        sum_value += value
        sum_value_accumulate.append(sum_value)
    return sum_value_accumulate
# Quick map convertion
def lm(*x): return list(map(*x))        # List of Map
def sm(*x): return set(map(*x))         # Set of Map
# Quick sum
def suml(*x): return sum(list(*x))      # Sum of List
def sumlm(*x): return suml(map(*x))     # Sum of List of Map
# Chemistry
# For calculate: pH pOH
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
# Natural log
def ln(x):
    return log(x, e)


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

    print(f'{colorama.Fore.RED}Score: {score}/{max_score}')
    print(f'{colorama.Fore.GREEN}Percent: {score_percentage:.2f}%')
