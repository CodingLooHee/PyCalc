# Lighter version of main.py #! Underdevelopment


# Normal import
from code import InteractiveConsole as _InteractiveConsole
from colorama import init as _colorama_init
from rich import pretty as _rich_pretty
from art import text2art

_colorama_init(autoreset=True)
_rich_pretty.install()  # Make output colorful


# Import to be use in console
from pycalc.dna2 import (
    UnknownBase,
    UnknownPrime,
    DNA,
    RNA,
    dna2rna,
    rna2dna,
    na_swap,
    oppose_dna,
    oppose_rna,
    transcript,
)
from pycalc.units import (
    yotta,
    zetta,
    exa,
    peta,
    tera,
    giga,
    mega,
    kilo,
    hecto,
    deca,
    deci,
    centi,
    milli,
    micro,
    nano,
    pico,
    femto,
    atto,
    zepto,
    yocto,
    to_yotta,
    to_zetta,
    to_exa,
    to_peta,
    to_tera,
    to_giga,
    to_mega,
    to_kilo,
    to_hecto,
    to_deca,
    to_deci,
    to_centi,
    to_milli,
    to_micro,
    to_nano,
    to_pico,
    to_femto,
    to_atto,
    to_zepto,
    to_yocto,
)
from pycalc.general import (
    RAD,
    RAD2,
    CWD,
    ke,
    qe,
    qp,
    G,
    rada,
    rad2deg,
    deg2rad,
    sina,
    cosa,
    tana,
    csca,
    seca,
    cota,
    asina,
    acosa,
    atana,
    c,
    acc,
    lm,
    sm,
    suml,
    sumlm,
    p,
    c_rate,
    root,
    dis2,
    dis3,
    ln,
    cmd,
    cls,
    scalc,
)

"""
# TODO: Make this import
matplotlib.pyplot
sympy (as sp)
pandas
random
math
statistics
"""
from random import random, randint, randrange
from math import sin, cos, tan, pi, floor, ceil, asin, acos, atan

if __name__ == "__main__":
    shell = _InteractiveConsole(globals().copy() | locals().copy())
    shell.interact(
        banner="--------------------------------------------\n"
        + text2art("PYCALC")
        + "--------------------------------------------"
    )
