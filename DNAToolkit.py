# DNA Toolkit file
import collections
from collections import Counter
from structures import *
from utilities import *

# Check if the sequence is a valid DNA string
def validate_seq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False 
    return tmpseq 

def nucleotide_frequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict 
    return dict(collections.Counter(seq))

def transcription(seq):
    """ DNA -> RNA Transcription. Replacing Thymine with Uracil."""
    return seq.replace('T', 'U')

def reverse_transcription(seq):
    """ RNA -> DNA.  Replacing Uracil with Thymine."""
    return seq.replace('U', 'T')

def complement(seq):
    """Swapping Adenine with Thymine, Guanine with Cytosine."""
    # comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # compSeq = ""
    # for nuc in seq:
    #     compSeq += comp[nuc]
    # return compSeq
    #return ''.join([DNA_Complement[nuc] for nuc in seq])
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)

def reverse_complement(seq):
    """
    Swapping Adenine with Thymine, Guanine with Cytosine. 
    Reversing generated string.
    """
    return complement(seq)[::-1]
    
def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

def gc_content_subseq(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res 

def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an amino acid sequence"""
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given amino acid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict

def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequence, including the reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames 


