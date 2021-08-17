import math 

def nCr(n,r):
    f = math.factorial 
    return f(n) / (f(r) * f(n-r))

ans = nCr(17,10) - nCr(6,3)*nCr(11,7) - nCr(12,7)*nCr(5,3) + nCr(6,3)*nCr(6,4)*nCr(5,3)

print(ans)