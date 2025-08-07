def find(search_list, value):
    cuenta = 0
    # comprobamos si la lista esta vacia 
    if not search_list:
        raise ValueError("value not in array")
    
    while True:
        # conseguimos la mitad de la lista
        mitad = len(search_list) // 2

        if len(search_list) == 1 and search_list[0] != value:
            raise ValueError("value not in array")
        
        # si encontramos el numero regresamos la cuenta +  la mitad
        elif search_list[mitad] == value:
            return cuenta + mitad
        # si la mitad de la lista es mayor que el valor borramos la segunda mitad
        elif search_list[mitad] > value:
            del search_list[mitad:]
        # si la mitad de la lista es menor que el valor borramos la primera mitad
        elif search_list[mitad] < value:
            cuenta += mitad # sumamos la mitad a la cuenta 
            del search_list[:mitad]