# To find the most frequent k-mers in the Genome e.g. will use OriC of Vibrio Cholerae

# Define Genome
Genome = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGAT
          AGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGC
          AATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACG
          AAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTA
          GCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCA
          TCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTA
          ACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'
          
# Define size of k-mer
k = 4

# Define function to find k-mer of maximum frequency
def maxKmer(Genome,k):
  kmer = []
  freq = freqMap(Genome, k)
  m = max(freq.values())
  for key in freq:
    if freq[key] == m:
      kmer.append(key)
  return kmer
  
 # Define function for frequency map
 def freqMap(Genome,k):
  freq = {}
  n = len(Genome)
  for i in range(n-k+1):
    Pattern = Genome[i:i+k]
    freq[Pattern] = 0
  for i in range(n-k+1):
    if Pattern == Text[i:i+k]:
      freq[Pattern] = freq[Pattern] + 1
  return freq
  
  # Print result
  print(maxKmer(Genome,k))
    
