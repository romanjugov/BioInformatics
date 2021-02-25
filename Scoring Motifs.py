# For a given list of Motifs, the script will generate a dictionary (count matrix) of all occurances of that base in the motifs on each position for the length of the motif
# The each element in the count matrix is then divided by the amount of rows in the count matrix

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
            
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = Count(Motifs)
    # insert your code here
    for i in profile:  
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile
