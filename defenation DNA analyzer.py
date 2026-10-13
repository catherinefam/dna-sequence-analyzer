def count_A(sequence):
    count_A= 0
    for base in sequence:
        if base =="A":
            count_A= count_A +1
    return count_A


def count_T(sequence):
    count_T = 0
    for base in sequence:
        if base =="T":
            count_T= count_T +1
    return count_T

def count_G(sequence):
    count_G = 0
    for base in sequence:
        if base == "G":
            count_G = count_G +1
    return count_G

def count_C(sequence):
    count_C = 0
    for base in sequence:
        if base == "C":
            count_C = count_C + 1
    return count_C


def gc_content(sequence):
    g = count_G(sequence)
    c = count_C(sequence)
    GC = g + c
    length =len(sequence)
    GC_percent = GC / length *100
    return GC_percent

sequence = input("enter DNA sequence:")
pattern = input("enter pattern:")
sequence_valid = True
pattern_valid = True
found = False
 
for base in sequence:
    if base not in "ATGC":
        sequence_valid = False 
for base in pattern:
    if base not in "ATGC":
        pattern_valid = False
if sequence_valid and pattern_valid:
    a = count_A(sequence)
    t = count_T(sequence)
    g = count_G(sequence)
    c = count_C(sequence)
    gc = gc_content(sequence)

    print ("A:" ,a)
    print ("T:" ,t)
    print ("G:" ,g)
    print ("C:" ,c)
    print ("GC%:" ,gc)
    
    for i in range (len(sequence) - len(pattern)+1):
        if sequence[i:i+len(pattern)] == pattern:
           print (i)
           found = True
    if not found:
        print ("pattern is not found")
else:
    print ("Invalid DNA sequence or pattern")