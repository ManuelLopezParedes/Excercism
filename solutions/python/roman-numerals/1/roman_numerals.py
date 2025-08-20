def roman(number):
    """Convierte un número entero decimal a su representación en números romanos. El valor máximo permitido es 3999."""
    # Lista ordenada de pares (valor, símbolo) para construir números romanos de forma descendente
    romanos = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
    ]

    # manejo de errores donde excedemos el limite numerico
    if number > 3999:
        raise ValueError("el valor agregado debe de ser menor o igual a 3999")
    
    # Inicializacion de variables
    i=0 # indice para recorrer la lista de valores romanos 
    res = "" # String donde guardamos el resultado final
    
    # Bucle que resta el mayor valor posible y concatena su símbolo romano al resultado
    while number:
        if number - romanos[i][0] >= 0:
            res += romanos[i][1]
            number  -= romanos[i][0]
        else:
            i += 1
    return res
