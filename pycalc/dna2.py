# DNA and RNA version 2

from typing import NoReturn, overload
import colorama as _colorama
from abc import ABCMeta, abstractmethod


# *Custom error
class UnknownBase(Exception):
    pass

class UnknownPrime(Exception):
    pass


# *Low level utility
# Check if sequence is valid
def _is_sequence_valid(sequence: str, allowedBase: list[str]) -> bool:
        for base in sequence:
            if not base in allowedBase:
                return False
        return True


def _sequence_check_with_raise(sequence: str, allowedBase: list[str]) -> str | NoReturn:
    ''' Check if sequence is valid
    Valid?    -> Return sequence
    Invalid?  -> Throw error
    '''

    # Ensure the sequence is string
    if type(sequence) != str:
        raise TypeError('The sequence must be string')

    sequence_upper_case = sequence.upper()

    if _is_sequence_valid(sequence_upper_case, allowedBase):
        return sequence_upper_case
    else:
        # Color unknown base in RED
        error_base = ''
        for base in sequence_upper_case:
            if base not in allowedBase:
                error_base += f'{_colorama.Fore.RED}{base}{_colorama.Fore.RESET}'
            else:
                error_base += base
        
        raise UnknownBase(f'Unknown base in sequence: {error_base}')


def _is_prime_valid(prime: int) -> bool:
    match prime:
        case 3 | 5:
            return True
        case _:
            return False


def _prime_check_with_raise(prime: int) -> int | NoReturn:
    if _is_prime_valid(prime):
        return prime
    else:
        raise UnknownPrime(f'Unknown prime: {prime}\'')


# *DNA and RNA
class _NA_Type(metaclass=ABCMeta):
    ALLOWED_BASE: list[str] = []

    def __init__(self, sequence: str='', start_prime: int=5) -> None:
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)
        self._start_prime = _prime_check_with_raise(start_prime)

    @abstractmethod
    def __repr__(self) -> str:
        return f'<NA {self._start_prime}\'- {self.value} {3 if self._start_prime == 5 else 3}\'>'

    def __str__(self) -> str:
        return self.__repr__()
    
    @property
    def value(self):
        return self._sequence
    
    @value.setter
    def value(self, sequence: str=''):
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)


class DNA(_NA_Type):
    ALLOWED_BASE = ['A','G','T','C']

    def __repr__(self) -> str:
        return f'<DNA {self._start_prime}\'- {self.value} -{3 if self._start_prime == 5 else 5}\'>'
    
    def copy(self):
        return DNA(self.value, self._start_prime)


class RNA(_NA_Type):
    ALLOWED_BASE = ['A','G','U','C']

    def __repr__(self) -> str:
        return f'<RNA {self._start_prime}\'- {self.value} -{3 if self._start_prime == 5 else 5}\'>'

    def copy(self):
        return RNA(self.value, self._start_prime)


#TODO: Make prime support for this
# *High level utility
def dna2rna(dna: DNA) -> RNA:
    if type(dna) != DNA:
        raise TypeError('Must be DNA')
    new_rna = RNA()
    new_rna.value = dna.value.replace('T', 'U')
    return new_rna

def rna2dna(rna: RNA) -> DNA:
    if type(rna) != RNA:
        raise TypeError('Must be RNA')
    new_dna = DNA()
    new_dna.value = rna.value.replace('U', 'T')
    return new_dna

@overload
def na_swap(na: DNA) -> DNA | NoReturn:...
@overload
def na_swap(na: RNA) -> RNA | NoReturn:...

def na_swap(na):
    if type(na) not in [DNA, RNA]:
        raise TypeError('Must be DNA or RNA')
    na.value = na.value[::-1]       # This modify the original value!
    return na

def oppose_dna(dna: DNA) -> DNA:
    new_dna = DNA()
    for base in dna.value:
        match base:
            case 'A':
                new_dna.value += 'T'
            case 'G':
                new_dna.value += 'C'
            case 'T':
                new_dna.value += 'A'
            case 'C':
                new_dna.value += 'G'
    return new_dna

def oppose_rna(rna: RNA) -> RNA:
    new_rna = RNA()
    for base in rna.value:
        match base:
            case 'A':
                new_rna.value += 'U'
            case 'G':
                new_rna.value += 'C'
            case 'U':
                new_rna.value += 'A'
            case 'C':
                new_rna.value += 'G'
    return new_rna

def transcript(dna: DNA) -> RNA:
    # Swap 5' and 3'
    # Oppose base
    # DNA -> RNA
    temp_dna = dna.copy()
    na_swap(temp_dna)
    temp_dna = oppose_dna(temp_dna)
    new_rna = dna2rna(temp_dna)
    return new_rna


# Test zone
if __name__ == '__main__':
    d = DNA('agtc')
    mr = transcript(d)
    print(mr.value)
