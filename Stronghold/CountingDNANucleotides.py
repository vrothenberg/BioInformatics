from DNAToolkit import *

with open("Stronghold\\rosalind_dna.txt") as f:
    seq = f.readline()
    f.close()



nucleotideCount = nucleotide_frequency(seq)

# result = ""
# for nt in Nucleotides:
#     result = result + str(nucleotideCount[nt]) + " "

print(' '.join([str(val) for key, val in nucleotideCount.items()]))