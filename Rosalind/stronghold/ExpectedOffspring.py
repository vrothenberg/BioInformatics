from utilities import readFile
from structures import dominant_phenotype_prob

alleles = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]

pairs = list(map(int, readFile("test_data/rosalind_iev.txt")[0].split(' ')))

result = 0

for i in range(len(alleles)):
    allele = alleles[i]
    #print(allele, dominant_phenotype_prob[allele])
    result += dominant_phenotype_prob[allele] * pairs[i] * 2 

print(result)

