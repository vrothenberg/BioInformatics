# DNA Toolkit file
import collections
from structures import *
from utilities import *

# Check if the sequence is a valid DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False 
    return tmpseq 

def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict 
    return dict(collections.Counter(seq))

def transcription(seq):
    """ DNA -> RNA Transcription. Replacing Thymine with Uracil."""
    return seq.replace('T', 'U')

def complement(seq):
    """Swapping Adenine with Thymine, Guanine with Cytosine."""
    # comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # compSeq = ""
    # for nuc in seq:
    #     compSeq += comp[nuc]
    # return compSeq
    return ''.join([DNA_Complement[nuc] for nuc in seq])

def reverseComplement(seq):
    """Swapping Adenine with Thymine, Guanine with Cytosine. Reversing generated string."""
    return complement(seq)[::-1]
    
