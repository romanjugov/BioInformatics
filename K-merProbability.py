# Function to find the most probable k-mer

def Pr(text, profile):
    n = len(text)
    k = len(profile)
    p = 1
    for i in range(n):
        symbol = text[i]
        p *= profile[symbol][i]
    return p

def ProfileMostProbableKmer(text, k, profile):
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
