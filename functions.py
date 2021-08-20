def composition_k(k, text):
    comps = []
    if k > len(text):
        return comps
    for i in range(len(text)-k+1):
        s = text[i:i+k]
        comps.append(s)
    return comps

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

