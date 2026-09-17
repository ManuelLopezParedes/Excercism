def sum_of_multiples(limit, multiples):
    lista = []

    # si hay un 0 lo ignoramos ya que no suma nada
    for item in multiples:
        if item == 0:
            continue

        i = 1
        # mulltiplicamos item hasta llegar a limit
        while True:
            total = item * i
            if total >= limit:
                i = 1
                break
            # agregamos a una lista
            lista.append(total)
            i += 1
    # eliminamos los duplicados y sumamos los elementos
    return sum(set(lista))