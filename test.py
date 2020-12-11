from DNAToolkit import *
import random

# validateSeq tests 
rndDNAstr = "ACTGGTTAA"
assert(validateSeq(rndDNAstr) == "ACTGGTTAA")
invalidDNAstr = "XGTAACC"
assert(validateSeq(invalidDNAstr) == False)
mixedCaseDNAstr = "aAttCcCgaTTaca"
assert(validateSeq(mixedCaseDNAstr) == mixedCaseDNAstr.upper())
randomDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(20)])
assert(validateSeq(randomDNAStr) != False)
print(randomDNAStr)
print(countNucFrequency(randomDNAStr))