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
            symbol = Motifs[i][j]         # Variable symbol is a single base in a motif
            count[symbol][j] += 1         # Add 1 to the count of a base occuring on the current position
    return count                          # Return count

# This generates an output below:
# {'A': [3, 3, 0, 0, 2, 2, 3, 0, 2, 2, 3, 0], 'C': [0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0], 'G': [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], 'T': [0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 3]}


# Define second function that divides each element in count matrix by the row number in the count matrix

def Profile(Motifs):                      # Take 1 arg (Motif list)
    t = len(Motifs)                       # Length of Motif list = 3
    k = len(Motifs[0])                    # Length of firs Motif in the Motif list = 12
    profile = {}                          # Set up Profile dictionary
    profile = Count(Motifs)               # Populate the dictionary with the results of the first function
    for i in profile:                     # For each element or each base A, C, G, T
        for j in range(k):                # For each element in count list
            profile[i][j] = profile[i][j]/t  # Take each element and divide by row number
    return profile                           # Return transformed data

# This generates an output below:
# {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0], 'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6], 'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0], 'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}

