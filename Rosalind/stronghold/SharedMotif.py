from utilities import FASTA_to_dict
from DNAToolkit import *

FASTA_dict = FASTA_to_dict("test_data/rosalind_lcsm.txt")

# print(longest_common_substring("GATTACA", "TAGACCA"))
# print(longest_common_substring("GATTACA", "ATACA"))
# print(longest_common_substring("TAGACCA", "ATACA"))

def findstem(arr):
 
    # Determine size of the array
    n = len(arr)
 
    # Take first word from array
    # as reference
    s = arr[0]
    l = len(s)
 
    res = ""
 
    for i in range(l):
        #print(i)
        for j in range(i + 1, l + 1):
            
            # generating all possible substrings
            # of our reference string arr[0] i.e s
            stem = s[i:j]
            k = 1
            for k in range(1, n):
                #print(i, j, k, stem)
 
                # Check if the generated stem is
                # common to all words
                if stem not in arr[k]:
                    #print(stem + " not in arr[" + str(k) + "]")
                    break
 
            # If current substring is present in
            # all strings and its length is greater
            # than current result
            if (k + 1 == n and len(res) < len(stem)):
                res = stem
 
    return res
 
arr = list(FASTA_dict.values())

stems = findstem(arr)
print(stems)



# FASTA_list_keys = list(FASTA_dict.keys())

# for i in range(len(FASTA_list_keys)):
#     s = FASTA_dict[FASTA_list_keys[i]]
#     for j in range(i+1, len(FASTA_list_keys)):
#         t = FASTA_dict[FASTA_list_keys[j]]
#         longest_common_substring(s, t)
#         quit()

