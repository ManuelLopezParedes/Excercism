def rebase(input_base, digits, output_base):
    # manejo de errores
    #comprobacion de base de entrada
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    # comprobacion de base de salida
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # comprobacion de digitos pertenezcan a la base inicial
    for i in digits:
        if 0 > i or i >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # inicializacion de variables
    exp = len(digits) - 1 # ajustamos el valor del exponente
    base10 = 0
    basex= []
    aux = []

    # convertimos input_base a base 10
    for i in digits:
        base10 += i * (input_base**exp)
        exp -= 1 

    # si output_base es igual a 10 nos ahorramos el codigo de abajo
    if output_base == 10:
        basex= [int(d) for d in str(base10)]
        return basex
    
    # si la base es 0 lo regresamos como lista
    if base10 == 0:
        return [0]
    
    # convertimos base10 a output_base
    while base10:
        basex.insert(0,base10 % output_base)
        base10 = base10//output_base

    return basex