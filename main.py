from DNAToolkit import *
from utilities import colored
import random 

# Main testing file

# Create random DNA sequence:
randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(100)])

DNAStr = validate_seq(randDNAStr)

print(f"\nSequence: {colored(DNAStr)}\n")
print(f"[1] + Sequence Length: {len(DNAStr)}\n")
print(colored(f'[2] + Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n'))
print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n")
print(f"[4] + DNA String + Complement:\n5' {colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(complement(DNAStr))} 5' [Complement]\n")

print(f"5' {colored(reverse_complement(DNAStr))} 3' [Rev. Complement]\n")

print(f"[5] + GC Content: {gc_content(DNAStr)}%\n")
print(f"[6] + GC Content in Subsection k=5: {gc_content_subseq(DNAStr, k=5)}\n")

print(f'[7] + Amino acids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')

print(f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')

print(f'[9] + Reading frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)