def mendel(k, m, n):
    # k = num homozygous dominant (YY) 
    # m = num heterozygous (Yy)
    # n = num homozygous recessive (yy)
    total = k + m + n
    YY_YY = (k/total) * ((k-1)/(total-1)) * (1)
    YY_Yy = (k/total) * (m/(total-1)) * (1)
    YY_yy = (k/total) * (n/(total-1)) * (1)
    Yy_YY = (m/total) * (k/(total-1)) * (1)
    Yy_Yy = (m/total) * ((m-1)/(total-1)) * (0.75)
    Yy_yy = (m/total) * (n/(total-1)) * (0.5)
    yy_YY = (n/total) * (k/(total-1)) * (1)
    yy_Yy = (n/total) * (m/(total-1)) * (0.5)
    prob_dominant_allele = (YY_YY + YY_Yy + YY_yy + Yy_YY + \
        Yy_Yy + Yy_yy + yy_YY + yy_Yy)
    return prob_dominant_allele

print(mendel(27,20,30))