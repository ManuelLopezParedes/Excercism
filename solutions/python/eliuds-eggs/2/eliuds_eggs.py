def egg_count(display_value):
    """convertir un numero a decimal y despues contar los 1"""
    huevos = 0
    
    # convertimmos el numero a decimal
    while display_value:
        if display_value % 2 == 1: # si el residuo es 1 suma un huevo
            huevos += 1
        display_value = display_value // 2 # dividimos el numero para la siguiente iteracion
    
    return huevos # regresamos los huevos totales