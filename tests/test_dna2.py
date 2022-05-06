import pytest
from pycalc.dna2 import *
from pycalc.dna2 import _NA_Type, _is_prime_valid, _prime_check_with_raise

# Test for DNA/RNA Init
def test_dna_init_1():
    dna = DNA()
def test_rna_init_1():
    rna = RNA()
def test_dna_init_2():
    dna = DNA('agtcagtcagtc')
def test_rna_init_2():
    rna = RNA('agcuagcuagcu')
def test_dna_init_null():
    dna = DNA('')
def test_rna_init_null():
    rna = RNA('')
@pytest.mark.xfail(raises=UnknownBase)
def test_dna_init_error():
    dna = DNA('agtcuagtcu')
@pytest.mark.xfail(raises=UnknownBase)
def test_rna_init_error():
    rna = RNA('agtcuagtcu')



# Test for _NA_Type abstract method
@pytest.mark.xfail(raises=TypeError)
def test_na_abc_1():
    class NA_new(_NA_Type):
        pass

    na = NA_new()

def test_na_abc_2():
    class NA_new(_NA_Type):
        def __repr__(self) -> str:
            return ''

    na = NA_new()



# Test for high level function
def test_dna2rna():
    d = DNA('agtcatcgct')
    assert dna2rna(d).value == 'agucaucgcu'.upper()

def test_rna2dna():
    r = RNA('ugagcuagcagcacuaucua')
    assert rna2dna(r).value == 'tgagctagcagcactatcta'.upper()

def test_na_swap_dna_1():
    d = DNA('agtccagctac')
    na_swap(d)
    assert d.value == 'catcgacctga'.upper()

def test_na_swap_dna_2():
    d = DNA('agtccagctac')
    d = na_swap(d)
    assert d.value == 'catcgacctga'.upper()

def test_na_swap_rna_1():
    r = RNA('aguccagcuac')
    na_swap(r)
    assert r.value == 'caucgaccuga'.upper()

def test_na_swap_rna_2():
    r = RNA('aguccagcuac')
    r = na_swap(r)
    assert r.value == 'caucgaccuga'.upper()

def test_oppose_dna():
    d = DNA('agtcagctcta')
    assert oppose_dna(d).value == 'tcagtcgagat'.upper()

def test_oppose_rna():
    r = RNA('agucagcucua')
    assert oppose_rna(r).value == 'ucagucgagau'.upper()

def test_transcript():
    template_dna = DNA('agtcagtcagcatcacgact')
    mrna = transcript(template_dna)
    assert mrna.value == 'agucgugaugcugacugacu'.upper()

def test_dna_copy():
    dna_original = DNA('agtc')
    dna_copied = dna_original.copy()
    assert dna_original.value == dna_copied.value

def test_rna_copy():
    rna_original = RNA('aguc')
    rna_copied = rna_original.copy()
    assert rna_original.value == rna_copied.value

# Copied dna must be deepcopy
# Changing the copied value must not change the original value 
def test_dna_copy_no_link():
    dna_original = DNA('agtc')
    dna_copied = dna_original.copy()
    dna_original.value = 'aaggttcc'
    assert dna_original.value != dna_copied.value

def test_rna_copy_no_link():
    rna_original = DNA('agtc')
    rna_copied = rna_original.copy()
    rna_original.value = 'aaggttcc'
    assert rna_original.value != rna_copied.value


# Test for low-level prime checker
def test_is_prime_valid_5():
    assert _is_prime_valid(5)


def test_is_prime_valid_3():
    assert _is_prime_valid(3)

@pytest.mark.xfail(raises=AssertionError)
def test_is_prime_valid_invalid():
    assert _is_prime_valid(4)


def test_prime_checker_5():
    assert _prime_check_with_raise(5) == 5


def test_prime_checker_3():
    assert _prime_check_with_raise(3) == 3

@pytest.mark.xfail(raises=UnknownPrime)
def test_prime_checker_invalid():
    _prime_check_with_raise(4)
