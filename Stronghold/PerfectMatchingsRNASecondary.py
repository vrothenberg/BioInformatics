from utilities import FASTA_to_dict
import math 

FASTA_dict = FASTA_to_dict("test_data/rosalind_pmch.txt")

seq = list(FASTA_dict.values())[0]

A = seq.count('A')
U = seq.count('U')
C = seq.count('C')
G = seq.count('G')

def nCr(n,r):
    f = math.factorial 
    return f(n) / (f(r) * f(n-r))


if A == U and C == G:
    print(round(nCr(A,1) * nCr(C,1)))
else:
    print("Unequal numbers of A and U or C and G")