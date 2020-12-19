from utilities import FASTA_to_dict
from math import factorial as f

FASTA_dict = FASTA_to_dict("test_data/rosalind_pmch.txt")

seq = list(FASTA_dict.values())[0]

A = seq.count('A')
U = seq.count('U')
C = seq.count('C')
G = seq.count('G')

if A == U and C == G:
    print(f(A) * f(C))
else:
    print("Unequal numbers of A and U or C and G")