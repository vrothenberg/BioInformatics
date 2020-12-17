from utilities import FASTA_to_dict

# Converting FASTAFile list data into dictionary
FASTA_dict = FASTA_to_dict("test_data/rosalind_grph.txt")

def suffix_prefix(s, t, k):
    """Returns true if suffix of length k in string s is 
    connected to prefix of length k in string t."""
    return s[-k:] == t[0:k]

adjacency_list = []

labels = list(FASTA_dict.keys())
for i in range(len(labels)):
    for j in range(len(labels)):
        if i != j and suffix_prefix(FASTA_dict[labels[i]], FASTA_dict[labels[j]], 3):
            adjacency_list.append(labels[i] + " " + labels[j])

for edges in adjacency_list:
    print(edges)

