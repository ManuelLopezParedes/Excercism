def factors(value):
    """regresa los factores primos de un número"""
    # creamos la lista donde guardaremos los factores
    facto = []
    # div sera el factor a dividir, inicialmente 2 porque 1 no se considera factor
    div = 2

    while True:
        # si el valor es 1 regresamos la lista
        if value == 1:
            return facto
        else:
            # si el modulo es 0 agregamos div a la lista
            if value % div == 0:
                value = value // div # actualizamos el valor de value
                facto.append(div)
            # si el modilo es diferente a 0 suma 1 a div
            else:
                div += 1
