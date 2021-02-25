# Output: The number of times Pattern appears in Text with at most d mismatches

# Set Genome and Pattern
Text = ''
Pattern = ''

# Alternatively import a text file with 3 lines containig Pattern[0], Genome[1] and mismatch distance d[3]
# import sys
# lines = sys.stdin.read().splitlines()
# print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))  # 

# Function to find count of pattern with d mismatch in Genome

def ApproximatePatternCount(Pattern, Text, d):              # Takes 3 args
    count = 0                                               # Initialize count variable at 0
    n = len(Text)                                           # Length of Genome
    k = len(Pattern)                                        # Length of Pattern
    for i in range(n-k+1):                                  # For length of Genome - Pattern +1
         if HammingDistance(Pattern, Text[i:i+k]) <= d:     # If the Hamming distance is <= d
                count += 1                                  # Add 1
    return count                                            # return count

# Hamming Distance function to count number of mismatches between Pattern and Genome

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
