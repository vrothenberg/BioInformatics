Nucleotides = ["A", "C", "G", "T"]

DNA_Complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

dominant_phenotype_prob = {
    'AA-AA' : 1.0,
    'AA-Aa' : 1.0,
    'AA-aa' : 1.0, 
    'Aa-Aa' : 0.75,
    'Aa-aa' : 0.5, 
    'aa-aa' : 0
}

monoisotopic_mass_table = {
    'A' :   71.03711,
    'C' :   103.00919,
    'D' :   115.02694,
    'E' :   129.04259,
    'F' :   147.06841,
    'G' :   57.02146,
    'H' :   137.05891,
    'I' :   113.08406,
    'K' :   128.09496,
    'L' :   113.08406,
    'M' :   131.04049,
    'N' :   114.04293,
    'P' :   97.05276,
    'Q' :   128.05858,
    'R' :   156.10111,
    'S' :   87.03203,
    'T' :   101.04768,
    'V' :   99.06841,
    'W' :   186.07931,
    'Y' :   163.06333
}