def square_root(number):
    lista = []
    for i in range(number + 1):
        lista.append(i)

    while True:
        # conseguimos la mitad de la lista
        mitad = len(lista) // 2

        if len(lista) == 1 and lista[0] ** 2 != number:
            raise ValueError("value not in array")
        
        # si encontramos el numero regresamos la cuenta +  la mitad
        elif lista[mitad] ** 2 == number:
            return lista[mitad]
        # si la mitad de la lista es mayor que el valor borramos la segunda mitad
        elif lista[mitad] ** 2 > number:
            del lista[mitad:]
        # si la mitad de la lista es menor que el valor borramos la primera mitad
        elif lista[mitad] ** 2 < number:
            del lista[:mitad]
