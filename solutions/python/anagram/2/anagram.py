def find_anagrams(word, candidates):
    # lista de anagramas
    final=[]
    # convertimos word a minusculas
    ord = word.lower()
    sort = sorted(ord)

    # recorremos las lista de candidatos
    for candidato in candidates:
        # convertimos al candidato a minusculas
        cand_ord = candidato.lower()
        # si ord es igual a cand_ord pasa al siguiente elemento de la lista
        if ord == cand_ord:
            continue
        # ordenamos alfabeticamente ambas cadenas y si son iguales agrega candidato a la lista
        if sorted(cand_ord) == sort:
            final.append(candidato)

    return(final)