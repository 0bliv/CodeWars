def DNA_strand(dna):
    complementary_strand = ""
    for base in dna:
        if base == "A":
            complementary_strand += "T"
        elif base == "T":
            complementary_strand += "A"
        elif base == "C":
            complementary_strand += "G"
        elif base == "G":
            complementary_strand += "C"
    return complementary_strand

