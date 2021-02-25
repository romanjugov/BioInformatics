# This algo compares two DNA strands (s1 and s2) of equal length and outputs the difference in bases as hamming distance

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
