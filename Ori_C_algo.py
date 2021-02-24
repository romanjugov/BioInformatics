# Input:  Strings Genome ('AACGTGAAGA') and symbol ('C')
# Output: A dictionary that shows the associated 'Value' of: the count of 'symbol' for each given window of size n//2 starting at position 'Key'. 

def FasterSymbolArray(Genome, symbol):               # function taking 2 args
    array = {}                                       # empty dictionary
    n = len(Genome)                                  # set variable n to length of genome
    Ext_Genome = Genome + Genome[0:n//2]             # genome + half of initial genome to account for wraparound and the large view window of len(n//2)
    
    array[0] = PatternCount(Genome[0:n//2], symbol)  # set count of viewing window of len(n//2) at position 0
    
    for i in range(1, n):                            # so as to not start at 0 index, loop from 1 -> n-1
        array[i] = array[i-1]                        # set the value of index to previous index value
        if Ext_Genome[i-1] == symbol:                # if you move past index position i,  and previous base was a match
            array[i] -= 1                            # subtract one from the count
        if Ext_Genome[i+(n//2)-1] == symbol:         # if you encounter a match on current base
            array[i] += 1                            # add one to the count
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text

def PatternCount(Text, Pattern):                     # function takes 2 args
    count = 0                                        # set count to 0
    k = len(Pattern)                                 # length of Pattern
    n = len(Text)                                    # length of genome
    for i in range(n-k+1):                           # loop over length of genome - length of window
        Test = Text[i:i+k]                           # test set for viewing window
        if Pattern == Test:                          # conditonal for match with pattern
            count += 1                               # if TRUE, add 1 to the count
    return count                                     # return count




with open('e_coli.txt') as file:                     # open genome file
    e_coli = file.read();

array = FasterSymbolArray(e_coli, "C")               # run function to look for 'C'

import matplotlib.pyplot as plt                      # import visualisation tool
plt.plot(*zip(*sorted(array.items())))               # plot the resulting graph of Cs
plt.show()
