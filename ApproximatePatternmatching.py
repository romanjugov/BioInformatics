# Function that utilises hamming distance to find list of positions where k-mer pattern matches a sequence, with at least d mismatches

# Initialise amount of mismatches
d = 1

def ApproximatePatternMatching(Genome, Pattern, d):         # Takes 2 args
    positions = []                                          # initializing list of positions
    n = len(Genome)                                         # Length of Genome
    k = len(Pattern)                                        # Length of Pattern
    for i in range(n-k+1):                                  # For length of Genome - Pattern +1
         if HammingDistance(Genome[i:i+k], Pattern) <= d:   # If hamming distance between pattern and genome is <= mismatch 
                positions.append(i)                         # Add position
    return positions                                        # Return result

# Insert your Hamming distance function on the following line.
def HammingDistance(s1, s2):                   # Takes 2 args
  n = len(s1)                                  # Length of s1
  k = len(s2)                                  # Length of s2
  if n == k:                                   # if strands of equal length
    HamDistance = 0                            # Set HamDistance to 0
    for i in range(n):                         # For range of s1 length
      if s1[i] != s2[i]:                       # If base on s1 is not equal to s2
        HamDistance += 1                       # Add 1
      else: "Strands must be of equal length"  # Otherwise error message
    return HamDistance
