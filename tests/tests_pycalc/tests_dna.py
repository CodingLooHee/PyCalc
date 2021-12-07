import pytest
from pycalc import dna
import pycalc


def tests_import():
    pycalc.dna


def tests_init():
    d = pycalc.dna.DNA(str_dna:='AGTCagtc')
    assert d.template == str_dna.upper()

