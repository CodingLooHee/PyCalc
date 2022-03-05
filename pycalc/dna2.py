# DNA and RNA version 2

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
        raise UnknownBase('Unknown base detected')


# *DNA and RNA
class _NA_Type:
    pass


class DNA(_NA_Type):
    ALLOWED_BASE = ['A','G','T','C']

    def __init__(self, sequence: str='') -> None:
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)

    @property
    def value(self):
        return self._sequence
    
    @value.setter
    def value(self, sequence: str=''):
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)


class RNA(_NA_Type):
    ALLOWED_BASE = ['A','G','U','C']

    def __init__(self, sequence: str='') -> None:
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)

    @property
    def value(self):
        return self._sequence
    
    @value.setter
    def value(self, sequence: str=''):
        self._sequence = _sequence_check_with_raise(sequence, self.ALLOWED_BASE)


# *High level utility
def dna2rna(dna: DNA):
    if type(dna) != DNA:
        raise TypeError('Must be DNA')
    new_rna = RNA()
    new_rna.value = dna.value.replace('T', 'U')
    return new_rna

def rna2dna(rna: RNA):
    if type(rna) != RNA:
        raise TypeError('Must be RNA')
    new_dna = DNA()
    new_dna.value = rna.value.replace('U', 'T')
    return new_dna

def na_swap(na: DNA | RNA):
    if type(na) not in [DNA, RNA]:
        raise TypeError('Must be DNA or RNA')
    na.value = na.value[::-1]



# Test zone
if __name__ == '__main__':
    r = RNA('AGUCCUGA')
    print(r.value)
    d = rna2dna(r)
    print(d.value)
