import utilities, functions

kmers = utilities.readFile('stepik\dataset_200_8.txt')

def de_bruijn_kmers(kmers):
    graph = {}
    for kmer in kmers:
        prefix = kmer[0:-1]
        suffix = kmer[1:]
        functions.insert(graph, prefix, suffix)
    
    output = ''
    keys = list(graph.keys())
    keys.sort()
    for key in keys:
        l = ','.join(graph[key])
        output += key + ' -> ' + l + '\n'
    return output

#print(de_bruijn_kmers(kmers))

utilities.writeFile('stepik\output.txt', de_bruijn_kmers(kmers))