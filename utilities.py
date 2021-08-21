def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'

def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def writeFile(filePath, output):
    f = open(filePath, 'w')
    f.write(output)
    f.close()


def FASTA_to_dict(filepath):
    """Convert FASTA formatted file to dictionary of string labels and genetic sequences."""
    FASTA_file = readFile(filepath)
    result = {}
    for line in FASTA_file:
        if '>' in line:
            FASTALabel = line[1:].rstrip()
            result[FASTALabel] = ""
        else:
            result[FASTALabel] += line.rstrip()
    return result 