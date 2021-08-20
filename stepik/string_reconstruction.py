import utilities

kmers = utilities.readFile('stepik/dataset_198_3.txt')

def string_reconstruction(kmers):
    s = list(kmers[0])
    for i in range(1, len(kmers)):
        s.append(kmers[i][-1])
    return ''.join(s)

print(string_reconstruction(kmers))


