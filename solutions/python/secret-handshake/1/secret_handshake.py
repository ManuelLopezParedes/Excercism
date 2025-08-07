def commands(binary_str):
    lista = []
    acciones = ["jump","close your eyes", "double blink", "wink"]
    
    for i in range(-1,-5,-1):
        if binary_str[i] == '1':
            lista.append(acciones[i])

    if binary_str[0] == '1':
        lista.reverse()
    return lista