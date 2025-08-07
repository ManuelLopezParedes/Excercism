def proteins(strand):
    res =[]
    for i in range(0,len(strand),3):
        cad = strand[i:i+3]
        if cad == "AUG": 
            res.append("Methionine")
        elif cad in ["UUU","UUC"]:
            res.append("Phenylalanine")
        elif cad in ["UUA","UUG"]:
            res.append("Leucine")
        elif cad in ["UCU","UCC","UCA","UCG"]:
            res.append("Serine")
        elif cad in ["UAU","UAC"]:
            res.append("Tyrosine")
        elif cad in ["UGU","UGC"]:
            res.append("Cysteine")
        elif cad == "UGG":
            res.append("Tryptophan")
        else: 
            break
    return res