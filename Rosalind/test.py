from DNAToolkit import *
import random

# validate_seq tests 
rndDNAstr = "ACTGGTTAA"
assert(validate_seq(rndDNAstr) == "ACTGGTTAA")
invalidDNAstr = "XGTAACC"
assert(validate_seq(invalidDNAstr) == False)
mixedCaseDNAstr = "aAttCcCgaTTaca"
assert(validate_seq(mixedCaseDNAstr) == mixedCaseDNAstr.upper())
randomDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(20)])
assert(validate_seq(randomDNAStr) != False)
print(randomDNAStr)
print(nucleotide_frequency(randomDNAStr))