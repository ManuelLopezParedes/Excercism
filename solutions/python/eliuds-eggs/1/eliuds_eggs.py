def egg_count(display_value):
    lista = []
    huevos = 0
    while display_value != 0:
        res = display_value % 2
        lista.append(res)
        display_value = display_value // 2

    for item in reversed(lista):
        if item == 1:
            huevos += 1
    
    return huevos
