# Insert your Count(Motifs) function here.
def Count(Motifs):
    count = {}                 # initializing the count dictionary
    k = len(Motifs[0])         # k = lenght of the 1st Motif 
    for symbol in "ACGT":      # list of symbols/bases
        count[symbol] = []     # place empty list as key value pair to each base/symbol
        for j in range(k):     # for the length of the motif
            count[symbol].append(0)    # Add place that amount of 0s into the empty list inside count{}
    t = len(Motifs)                    # Length of motif list 
    for i in range(t):                 # for amount of elements in this list Motifs[i]
        for j in range(k):             # for length of bases in each 'element' Motifs[i][j]
            symbol = Motifs[i][j]      # Where symbol/base key matches base on Motif
            count[symbol][j] += 1      # Add 1 to count of each position
    return count                       # return matrix of counts e.g. {A:[1,2,0,1,2],C:[0,1,1,1,0]}

def Consensus(Motifs):                 
    k = len(Motifs[0])                # k = lenght of the 1st Motif
    count = Count(Motifs)             # run Count(Motif) method above
    consensus = ""                    # initialise empty string
    for j in range(k):                # for the length of the motif
        m = 0                         # initialise count at 0
        frequentSymbol = ""           # initialise empty string
        for symbol in "ACGT":         # for each symbol/base in list
            if count[symbol][j] > m:  # if count of each base in Motifs[i][j] is > 0
                m = count[symbol][j]  # make the current count of each base in Motifs[i][j] as m
                frequentSymbol = symbol  # make that base the most frequent base
        consensus += frequentSymbol      # add this base to consensus sequence
    return consensus                     # return full consensus sequence

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.

def Score(Motifs):                      
    consensus = Consensus(Motifs)        # Consensus(Motif) method above
    count = 0                            # initialise count at 0
    for motif in Motifs:                 # for each motif
        for index in range(len(motif)):  # for each position in length of a motif
            if motif[index] != consensus[index]: # if the index does not match the consensus index
                count += 1                       # add 1
    return count                                 # return consensus count of consensus sequence
