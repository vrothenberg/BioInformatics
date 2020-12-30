from DNAToolkit import gc_content
from utilities import readFile
import math 

contents = readFile("test_data/rosalind_prob.txt")

seq = contents[0]

A = [float(x) for x in contents[1].split(' ')]

#print(seq, A)

gc = A[0]

res = 1

B = []

for gc in A:
    res = 1
    for bp in seq:
        if bp in "GC":
            res *= (gc/2.0)
        else:
            res *= ((1-gc)/2.0)
    B.append(round(math.log10(res), 3))
    


print(" ".join(map(str, B)))
