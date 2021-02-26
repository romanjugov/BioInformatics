# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
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

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    for i in 'ACTG':
        for j in range(k):
            profile[i][j] = profile[i][j]/t  
    return profile

def Score(Motifs):                      
    consensus = Consensus(Motifs)        # Consensus(Motif) method above
    count = 0                            # initialise count at 0
    for motif in Motifs:                 # for each motif
        for index in range(len(motif)):  # for each position in length of a motif
            if motif[index] != consensus[index]: # if the index does not match the consensus index
                count += 1                       # add 1
    return count                                 # return consensus count of consensus sequence
# Then copy your ProfileMostProbableKmer(Text, k, Profile) and Pr(Text, Profile) functions here.
def Pr(text, profile):
    n = len(text)
    k = len(profile)
    p = 1
    for i in range(n):
        symbol = text[i]
        p *= profile[symbol][i]
    return p

def ProfileMostProbablePattern(text, k, profile):
    n = len(text)
    pr = {}
    most_prob_kmer = []
    for i in range(n-k+1):
        k_mer = text[i:i+k]
        probability = Pr(k_mer, profile)
        pr[k_mer] = probability
    m = max(pr.values())
    for key, value in pr.items():
        if pr[key] == m:
            most_prob_kmer.append(key)
    return most_prob_kmer[0]

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
    return BestMotifs
