import utilities

kmers = utilities.readFile('stepik\dataset_198_10.txt')

def insert(d, k, v):
    if k not in d:
        d[k] = [v]
    else:
        d[k].append(v)

def overlap_graph(kmers):
    prefixes = {}
    for kmer in kmers:
        prefix = kmer[0:-1]
        insert(prefixes, prefix, kmer)

    output = ''
    for kmer in kmers:
        suffix = kmer[1:]
        if suffix in prefixes:
            output += kmer + ' -> ' + ','.join(prefixes[suffix]) + '\n'

    return output

f = open('stepik/output.txt', 'w')
f.write(overlap_graph(kmers))
f.close()