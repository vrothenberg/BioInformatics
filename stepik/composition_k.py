import utilities

lines = utilities.readFile('stepik/dataset_197_3.txt')
k, text = lines 

#k = 5
#text = 'CAATCCAAC'
k = (int)(k)

def composition_k(k, text):
    comps = []
    if k > len(text):
        return comps
    for i in range(len(text)-k+1):
        s = text[i:i+k]
        comps.append(s)
    return comps

output = "\n".join(composition_k(k, text))
f = open('stepik/output.txt', 'w')
f.write(output)
f.close()