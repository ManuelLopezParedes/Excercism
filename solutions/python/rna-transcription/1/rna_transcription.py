def to_rna(dna_strand):
    lista = ""
    for dna in dna_strand:
        if dna == 'G':
            lista += 'C'
        elif dna == 'C':
            lista += 'G'
        elif dna == 'T':
            lista += 'A' 
        elif dna == 'A':
            lista += 'U' 
    return lista
    
