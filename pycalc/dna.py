
#! Deprecated

from pycalc import n_base


class RNA:
    def __init__(self, init_dna: str='') -> None:
        # Turn list into dna
        self.rna_template = self._str2rna(init_dna)
        
        # Getting non template dna
        self.rna_non_template = self._get_rna_oppose(self.rna_template)
    
    def __str__(self) -> str:
        return f'{self.template}'
        
    '''
    Please note that everytime something make change to the DNA sequence
    Non-template DNA must be changed oppose to template DNA and vice versa
    '''

    @property
    def template(self):                     # Get DNA in string format
        str_rna = ''
        for each_base in self.rna_template:
            str_rna += self._base2char(each_base)
        return str_rna
    
    @property
    def non_template(self):                 # Get non template DNA with string format
        str_rna = ''
        for each_base in self.rna_non_template:
            str_rna += self._base2char(each_base)
        return str_rna
    

    @template.setter    # type: ignore
    def template(self, new_rna: str):       # Set DNA with string format
        self.rna_template = self._str2rna(new_rna)
        self.rna_non_template = self._get_rna_oppose(self.rna_template)
    
    @non_template.setter    # type: ignore
    def non_template(self, new_rna:str):    # Set not template DNA with string format
        self.rna_non_template = self._str2rna(new_rna)
        self.rna_template = self._get_rna_oppose(self.rna_non_template)
    
    def transcript_from(self, dna):    # Accually more like mRNA #! Can't use DNA annotation because it's not define (It's define later)
        self.template = dna.non_template.replace('T', 'U')


    # Utility zone

    @staticmethod
    def _str2rna(str_rna: str):
        # Check if init_dna is string
        if type(str_rna) is not str:
            raise TypeError('This is not string')
        
        dna_template: list[n_base.N_BASE] = []
        # Turn list into dna
        for each_base in str_rna:
            match each_base:
                case 'A' | 'a':
                    dna_template.append(n_base.N_BASE.A)
                case 'G' | 'g':
                    dna_template.append(n_base.N_BASE.G)
                case 'U' | 'u':
                    dna_template.append(n_base.N_BASE.U)
                case 'C' | 'c':
                    dna_template.append(n_base.N_BASE.C)
                case _:
                    raise ValueError('Only A G U C can be put')
        return dna_template
    
    @staticmethod
    def _get_rna_oppose(str_rna: list[n_base.N_BASE]):
        # Getting non template dna
        dna_non_template: list[n_base.N_BASE] = []
        for each_base in str_rna:
            match each_base:
                case n_base.N_BASE.A:
                    dna_non_template.append(n_base.N_BASE.U)
                case n_base.N_BASE.U:
                    dna_non_template.append(n_base.N_BASE.A)
                case n_base.N_BASE.G:
                    dna_non_template.append(n_base.N_BASE.C)
                case n_base.N_BASE.C:
                    dna_non_template.append(n_base.N_BASE.G)
        return dna_non_template
    
    @staticmethod
    def _base2char(base_single: n_base.N_BASE):
        match base_single:
            case n_base.N_BASE.A:
                return 'A'
            case n_base.N_BASE.G:
                return 'G'
            case n_base.N_BASE.U:
                return 'U'
            case n_base.N_BASE.C:
                return 'C'
            case _:
                raise ValueError('Not an N_BASE')



class DNA:
    def __init__(self, init_dna: str='') -> None:
        # Turn list into dna
        self.dna_template = self._str2dna(init_dna)
        
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
    

    @template.setter    # type: ignore
    def template(self, new_dna: str):       # Set DNA with string format
        self.dna_template = self._str2dna(new_dna)
        self.dna_non_template = self._get_dna_oppose(self.dna_template)
    
    @non_template.setter    # type: ignore
    def non_template(self, new_dna:str):    # Set not template DNA with string format
        self.dna_non_template = self._str2dna(new_dna)
        self.dna_template = self._get_dna_oppose(self.dna_non_template)
    
    #? Check if it's work
    def reverse_from(self, mrna:RNA):
        self.template = mrna.non_template.replace('U', 'T') # type: ignore


    # Utility zone

    @staticmethod
    def _str2dna(str_dna: str):
        # Check if init_dna is string
        if type(str_dna) is not str:
            raise TypeError('This is not string')
        
        dna_template: list[n_base.N_BASE] = []
        # Turn list into dna
        for each_base in str_dna:
            match each_base:
                case 'A' | 'a':
                    dna_template.append(n_base.N_BASE.A)
                case 'G' | 'g':
                    dna_template.append(n_base.N_BASE.G)
                case 'T' | 't':
                    dna_template.append(n_base.N_BASE.T)
                case 'C' | 'c':
                    dna_template.append(n_base.N_BASE.C)
                case _:
                    raise ValueError('Only A G T C can be put')
        return dna_template
    
    @staticmethod
    def _get_dna_oppose(str_dna: list[n_base.N_BASE]):
        # Getting non template dna
        dna_non_template: list[n_base.N_BASE] = []
        for each_base in str_dna:
            match each_base:
                case n_base.N_BASE.A:
                    dna_non_template.append(n_base.N_BASE.T)
                case n_base.N_BASE.T:
                    dna_non_template.append(n_base.N_BASE.A)
                case n_base.N_BASE.G:
                    dna_non_template.append(n_base.N_BASE.C)
                case n_base.N_BASE.C:
                    dna_non_template.append(n_base.N_BASE.G)
        return dna_non_template
    
    @staticmethod
    def _base2char(base_single: n_base.N_BASE):
        match base_single:
            case n_base.N_BASE.A:
                return 'A'
            case n_base.N_BASE.G:
                return 'G'
            case n_base.N_BASE.T:
                return 'T'
            case n_base.N_BASE.C:
                return 'C'
            case _:
                raise ValueError('Not an N_BASE')
