import pytest
import pycalc
from pycalc.dna import *

def tests_version():
    assert pycalc.__version__ == '0.1.0'

def tests_dna():
    def init():
        dna = DNA(str_dna:='AGTCagtc')
        assert dna.template == str_dna
