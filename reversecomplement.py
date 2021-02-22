# Define string
Pattern = 'ACTGACTAAGGCCATA'

# Define function to reverse string and give complement
def Complement(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G", "N":"N"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement
    
# Print result    
print(Complement(Pattern))
