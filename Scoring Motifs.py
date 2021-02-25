# For a given list of Motifs, the script will generate a dictionary (count matrix) of all occurances of that base in the motifs on each position for the length of the motif
# The each element in the count matrix is then divided by the amount of rows in the count matrix


# Example lists of motifs
Motifs = ['AACTAAACAAAT','AACTAAACGGAT','AATTGGACAAAT']

# Define function that generates a base count

def Count(Motifs):                        # Takes 2 args
    count = {}                            # Generate count dictionary
    k = len(Motifs[0])                    # For length of first motif AACTAAACAAAT... in this case 12
    for symbol in "ACGT":                 # Symbol can be replaced by i, means for a base in this string 'ACGT'
        count[symbol] = []                # Count each symbol in the list of bases and generate another list
        for j in range(k):                # For every base in a motif
            count[symbol].append(0)       # Populate each list in the dictionary with 0
                                          
# This generates an output below:
# {'A': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'T': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

    t = len(Motifs)                       # For the amount of elements in the list , in this case 3 elements
    for i in range(t):                    # for each element in this list
        for j in range(k):                # For each base in a motif (equal to first elemennt lenght, can be any as all the motifs are equal length)
            symbol = Motifs[i][j]         # Variable symbol is the 
            count[symbol][j] += 1
    return count


# Define second function that divides each element in count matrix by the row number in the count matrix

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
