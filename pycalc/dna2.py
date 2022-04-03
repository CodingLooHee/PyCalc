# DNA and RNA version 2

import colorama as _colorama
from abc import abstractmethod


# *Custom error
class UnknownBase(Exception):
    pass


# *Low level utility
# Check if sequence is valid
def _is_sequence_valid(sequence: str, allowedBase: list[str]):
        for base in sequence:
            if not base in allowedBase:
                return False
        return True


def _sequence_check_with_raise(sequence: str, allowedBase: list[str]):
    ''' Check if sequence is valid
    Valid?    -> Return sequence
    Invalid?  -> Throw error
    '''
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


# *DNA and RNA
class _NA_Type:
    ALLOWED_BASE: list[str] = []

    def __init__(self, sequence: str='') -> None:
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)

    @abstractmethod
    def __repr__(self) -> str:
        return f'<NA {self.value}>'

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
        return f'<DNA "{self.value}">'
    
    def copy(self):
        return DNA(self.value)


class RNA(_NA_Type):
    ALLOWED_BASE = ['A','G','U','C']

    def __repr__(self) -> str:
        return f'<RNA "{self.value}">'

    def copy(self):
        return RNA(self.value)


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

def na_swap(na: DNA | RNA) -> DNA | RNA:
    if type(na) not in [DNA, RNA]:
        raise TypeError('Must be DNA or RNA')
    na.value = na.value[::-1]       # This modify the original value!
    return na.value

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
