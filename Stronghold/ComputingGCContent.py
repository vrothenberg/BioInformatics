from DNAToolkit import gc_content
from utilities import readFile
pat ='>Rosalind_'

# Store file contents in a list
FASTAFile = readFile("test_data/rosalind_gc.txt")
# Dictionary for labels + data 
FASTADict = {}
# String for current lable 
FASTALabel = ""

# Converting FASTAFile list data into dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line[1:].rstrip()
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line.rstrip()


# Dictionary comprehension to generate new dictionary with GC content values
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

# Look for max value
MaxGCKey = max(RESULTDict, key=RESULTDict.get)

# Print max GC content label and percentage
print(f'{MaxGCKey}\n{RESULTDict[MaxGCKey]}')
