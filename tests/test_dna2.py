import pytest
from pycalc.dna2 import *
from pycalc.dna2 import _NA_Type
from pycalc.dna2 import _is_sequence_valid, _sequence_check_with_raise
from pycalc.dna2 import _is_prime_valid, _prime_check_with_raise


# *Test for DNA/RNA Init
class TestNaInit:
    def test_dna_init_1(self):
        dna = DNA()
    def test_rna_init_1(self):
        rna = RNA()
    def test_dna_init_2(self):
        dna = DNA('agtcagtcagtc')
    def test_rna_init_2(self):
        rna = RNA('agcuagcuagcu')
    def test_dna_init_emptystr(self):
        dna = DNA('')
    def test_rna_init_emptystr(self):
        rna = RNA('')
    @pytest.mark.xfail(raises=UnknownBase)
    def test_dna_init_error(self):
        dna = DNA('agtcuagtcu')
    @pytest.mark.xfail(raises=UnknownBase)
    def test_rna_init_error(self):
        rna = RNA('agtcuagtcu')


# *Test for _NA_Type abstract method
class TestNATypeABC:
    @pytest.mark.xfail(raises=TypeError)
    def test_na_abc_1(self):
        class NA_new(_NA_Type):
            pass
        na = NA_new()
    def test_na_abc_2(self):
        class NA_new(_NA_Type):
            def __repr__(self) -> str:
                return ''
        na = NA_new()


# *Test for high level function
class TestNAConvert:
    def test_dna2rna(self):
        d = DNA('agtcatcgct')
        assert dna2rna(d).value == 'agucaucgcu'.upper()
    def test_rna2dna(self):
        r = RNA('ugagcuagcagcacuaucua')
        assert rna2dna(r).value == 'tgagctagcagcactatcta'.upper()

class TestNASwap:
    class TestSwappedSequence:
        def test_na_swap_dna_1(self):
            d = DNA('agtccagctac')
            na_swap(d)
            assert d.value == 'catcgacctga'.upper()
        def test_na_swap_dna_2(self):
            d = DNA('agtccagctac', start_prime=3)
            d = na_swap(d)
            assert d.value == 'catcgacctga'.upper()
        def test_na_swap_rna_1(self):
            r = RNA('aguccagcuac')
            na_swap(r)
            assert r.value == 'caucgaccuga'.upper()
        def test_na_swap_rna_2(self):
            r = RNA('aguccagcuac', start_prime=3)
            r = na_swap(r)
            assert r.value == 'caucgaccuga'.upper()

    class TestSwappedPrime:
        def test_na_swap_dna_prime_3to5(self):   # Test prime swap
            d = DNA('agtccagctac', start_prime=3)
            d = na_swap(d)
            assert d.prime == 5
        def test_na_swap_dna_prime_5to3(self):   # Test prime swap
            d = DNA('agtccagctac', start_prime=5)
            d = na_swap(d)
            assert d.prime == 3
        def test_na_swap_rna_prime_3to5(self):   # Test prime swap
            r = RNA('aguccagcuac', start_prime=3)
            r = na_swap(r)
            assert r.prime == 5
        def test_na_swap_rna_prime_5to3(self):   # Test prime swap
            r = RNA('aguccagcuac', start_prime=5)
            r = na_swap(r)
            assert r.prime == 3


class TestOppose:
    class TestOpposedSequence:
        def test_oppose_dna(self):
            d = DNA('agtcagctcta')
            assert oppose_dna(d).value == 'tcagtcgagat'.upper()
        def test_oppose_rna(self):
            r = RNA('agucagcucua')
            assert oppose_rna(r).value == 'ucagucgagau'.upper()

    # Make sure prime is not changed
    class TestPrimeLocked:
        def test_oppose_dna_prime_5(self):
            d = DNA('agtcagctcta', start_prime=5)
            assert oppose_dna(d).prime == 5
        def test_oppose_dna_prime_3(self):
            d = DNA('agtcagctcta', start_prime=3)
            assert oppose_dna(d).prime == 3
        def test_oppose_rna_prime_5(self):
            r = RNA('agucagcucua', start_prime=5)
            assert oppose_rna(r).prime == 5
        def test_oppose_rna_prime_3(self):
            r = RNA('agucagcucua', start_prime=3)
            assert oppose_rna(r).prime == 3


class TestTranscript:
    def test_transcript(self):
        template_dna = DNA('agtcagtcagcatcacgact')
        mrna = transcript(template_dna)
        assert mrna.value == 'agucgugaugcugacugacu'.upper()
    def test_transcript_prime_5to3(self):
        template_dna = DNA('aGtCCa', start_prime=5)
        transcripted = transcript(template_dna)
        assert transcripted.prime == 3
    def test_transcript_prime_3to5(self):
        template_dna = DNA('aGtCCa', start_prime=3)
        transcripted = transcript(template_dna)
        assert transcripted.prime == 5


class TestNACopy:
    def test_dna_copy(self):
        dna_original = DNA('agtc')
        dna_copied = dna_original.copy()
        assert dna_original.value == dna_copied.value
    def test_rna_copy(self):
        rna_original = RNA('aguc')
        rna_copied = rna_original.copy()
        assert rna_original.value == rna_copied.value

    # Copied dna must be deepcopy
    # Changing the copied value must not change the original value 
    def test_dna_copy_no_link(self):
        dna_original = DNA('agtc')
        dna_copied = dna_original.copy()
        dna_original.value = 'aaggttcc'
        assert dna_original.value != dna_copied.value
    def test_rna_copy_no_link(self):
        rna_original = DNA('agtc')
        rna_copied = rna_original.copy()
        rna_original.value = 'aaggttcc'
        assert rna_original.value != rna_copied.value


# Test for low-level prime checker
class TestPrime:
    class TestLowLevelPrimeChecker:
        def test_is_prime_valid_5(self):
            assert _is_prime_valid(5)
        def test_is_prime_valid_3(self):
            assert _is_prime_valid(3)
        @pytest.mark.xfail(raises=AssertionError)
        def test_is_prime_valid_invalid(self):
            assert _is_prime_valid(4)

    class TestPrimeCheckerWithRaiser:
        def test_prime_checker_5(self):
            assert _prime_check_with_raise(5) == 5
        def test_prime_checker_3(self):
            assert _prime_check_with_raise(3) == 3
        @pytest.mark.xfail(raises=UnknownPrime)
        def test_prime_checker_invalid(self):
            _prime_check_with_raise(4)

    class TestHighLevelPrime:
        class TestNAPrimeInit:
            def test_dna_prime_init_3(self):
                d = DNA(start_prime=3)
            def test_dna_prime_init_5(self):
                d = DNA(start_prime=5)
            def test_rna_prime_init_3(self):
                r = RNA(start_prime=3)
            def test_rna_prime_init_5(self):
                r = RNA(start_prime=5)
            @pytest.mark.xfail(raises=UnknownPrime)
            def test_dna_prime_init_fail(self):
                d = DNA(start_prime=4)
            @pytest.mark.xfail(raises=UnknownPrime)
            def test_rna_prime_init_fail(self):
                r = RNA(start_prime=4)
            @pytest.mark.xfail(raises=TypeError)
            def test_dna_prime_init_type_fail(self):
                d = DNA(start_prime='x')
            @pytest.mark.xfail(raises=TypeError)
            def test_rna_prime_init_type_fail(self):
                r = RNA(start_prime='x')

        class TestNAPrimeProperty:
            def test_dna_prime_getter(self):
                d = DNA(start_prime=3)
                assert d.prime == 3
            def test_rna_prime_getter(self):
                r = RNA(start_prime=3)
                assert r.prime == 3
            def test_dna_prime_setter(self):
                d = DNA(start_prime=5)
                d.prime = 3
                assert d.prime == 3
            def test_rna_prime_setter(self):
                r = RNA(start_prime=5)
                r.prime = 3
                assert r.prime == 3
            @pytest.mark.xfail(raises=UnknownPrime)
            def test_dna_prime_setter_invalid(self):
                d = DNA(start_prime=5)
                d.prime = 4
            @pytest.mark.xfail(raises=UnknownPrime)
            def test_rna_prime_setter_invalid(self):
                r = RNA(start_prime=5)
                r.prime = 4

