import urllib.request 
import re
from utilities import readFile

FASTA_dict = {}
protein_id_list = readFile("test_data/rosalind_mprt.txt")

#protein_id_list = ["P07204_TRBM_HUMAN"]

for protein in protein_id_list:
    url = "https://www.uniprot.org/uniprot/" + protein + ".fasta"
    FASTA_page = urllib.request.urlopen(url)
    FASTA_str = FASTA_page.read().decode("utf-8")
    FASTA_list = FASTA_str.split("\n")

    for line in FASTA_list:
        if '>' in line:
            #print("LABEL: ", line)
            #FASTALabel = line[1:].rstrip()
            FASTA_dict[protein] = ""
        else:
            #print("ELSE: ", line)
            FASTA_dict[protein] += line.rstrip()


FASTA_keys = sorted(list(FASTA_dict.keys()))
#print(FASTA_keys)


for key in FASTA_keys:
    #result = re.findall("N[^P][ST][^P]", seq).
    seq = FASTA_dict[key]
    p = re.compile("(?=(N[^P][ST][^P]))")
    iterator = p.finditer(seq)
    results = []
    for match in iterator:
        #print(match.span())
        results.append(str(match.span()[0] + 1))
    if len(results) >= 1:
        print(key)
        print(" ".join(results))

    #print(m.group())
    #print(result)


