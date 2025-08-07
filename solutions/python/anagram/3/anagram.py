def find_anagrams(word, candidates):
    # lista de anagramas
    final=[]
    # convertimos word a minusculas
    ord = word.lower()
    # ordenamos alfabeticamente word
    sort = sorted(ord)

    # recorremos las lista de candidatos
    for candidato in candidates:
        # convertimos al candidato a minusculas
        cand_ord = candidato.lower()
        # ordenamos alfabeticamente ambas cadenas y si son iguales agrega candidato a la lista
        if sorted(cand_ord) == sort and ord != cand_ord:
            final.append(candidato)

    return(final)