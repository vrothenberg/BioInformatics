from utilities import readFile
import numpy as np

FASTA_file = readFile("test_data/rosalind_cons.txt")
#print(file_list)

FASTA_dict = {}

# Converting FASTAFile list data into dictionary
for line in FASTA_file:
    if '>' in line:
        FASTALabel = line[1:].rstrip()
        FASTA_dict[FASTALabel] = ""
    else:
        FASTA_dict[FASTALabel] += line.rstrip()


labels = list(FASTA_dict.keys())

str_len = len(FASTA_dict[labels[0]])

profile_matrix = np.zeros((4,str_len), dtype=np.int8)

nuc_map = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}

for seq in FASTA_dict.values():
    #print(seq)
    for i in range(str_len):
        curr_char = seq[i]
        nuc_row = nuc_map[seq[i]]
        profile_matrix[nuc_row][i] += 1
        #print(curr_char, nuc_row, profile_matrix[nuc_row][i])
        #print(profile_matrix[nuc_row])
    #print(profile_matrix)
        
nucleotides = ['A', 'C', 'G', 'T']

#print(profile_matrix)

consensus = ""

for col in range(str_len):
    nuc = 'A'
    nuc_max = 0
    for row in range(4):
        if profile_matrix[row][col] > nuc_max:
            nuc_max = profile_matrix[row][col]
            nuc = nucleotides[row]
    consensus += nuc

print(consensus)
for row in range(4):
    #[" ".join(item) for item in profile_matrix[row].astype(str)]
    print(nucleotides[row] + ": " + " ".join(profile_matrix[row].astype(str)))
    