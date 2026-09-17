def sum_of_multiples(limit, multiples):
    lista = []
    for item in multiples:
        if item == 0:
            continue
        i = 1
        while True:
            total = item * i
            if total >= limit:
                i = 1
                break
            lista.append(total)
            i += 1
    lista = set(lista)
    return sum(lista)