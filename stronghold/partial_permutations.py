from math import factorial as fact

def partial_permutations(n, k):
    ''' Returns the total number of partial permutations P(n,k) modulo 1,000,000 ''' 
    res = fact(n) / fact(n-k)
    return round(res % 1000000)

print(partial_permutations(88,10))

