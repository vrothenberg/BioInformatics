from DNAToolkit import *

def recurrence(n, k):
    adults = [0] * n 
    babies = [0] * n
    adults[0] = 1 
    for i in range(1, n):
        babies[i] = adults[i-1] * k 
        adults[i] = adults[i-1] + babies[i-1]
    return adults[n-1]




print(recurrence(33, 2))