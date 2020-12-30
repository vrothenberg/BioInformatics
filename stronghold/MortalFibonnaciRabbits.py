from DNAToolkit import *

def recurrence(n, m):
    """n total months, m lifespan of rabbits in months"""
    adults = [0] * (n+1)
    babies = [0] * (n+1)
    babies[1] = 1
    for i in range(2, n+1):
        babies[i] = adults[i-1] 
        adults[i] = adults[i-1] + babies[i-1] 
        if i-m > 0:
            adults[i] -= babies[i-m]
    #print(adults)
    #print(babies)
    return adults[n] + babies[n]


print(recurrence(93, 19))