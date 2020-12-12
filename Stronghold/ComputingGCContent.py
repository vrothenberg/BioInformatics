from DNAToolkit import *

pat ='>Rosalind_'

data = {}

curr = ""

f = open("Stronghold//rosalind_gc.txt", "r")
for line in f:
    if pat in line:
        curr = line[1:].rstrip()
        data[curr] = ""
    else:
        data[curr] += line.rstrip()

f.close()

max_key = ""
max_gc = 0

for key, seq in data.items():
    if gc_content(seq) > max_gc:
        max_gc = gc_content(seq)
        max_key = key 

print(f'{max_key}\n{max_gc}')




#DNAStr = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

#print(gc_content(DNAStr))