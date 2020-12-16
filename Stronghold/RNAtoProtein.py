from DNAToolkit import *
from utilities import readFile

lines = readFile("test_data/rosalind_prot.txt")
#print(lines)

#RNA = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
RNA = lines[0]
DNA = reverse_transcription(RNA)

print("".join(translate_seq(DNA))[0:-1])