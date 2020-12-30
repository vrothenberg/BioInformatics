from itertools import permutations

def permute_to_list(n):
    f = open("Rosalind/output.txt", "w")
    nums = [i for i in range(1, n+1)]
    perm_list = list(permutations(nums))
    f.write(str(len(perm_list)) + "\n")
    for p in perm_list:
        f.write(' '.join(list(map(str,p))) + "\n")
    f.close()

permute_to_list(5)