def is_valid(isbn):
    sin_guion = isbn.lower().replace("-", "")
    bandera = False 

    if len(sin_guion) == 10 and sin_guion[-1] == "x":
        bandera = True

    lista = []
    for caracter in sin_guion:
        if caracter.isdigit():
            lista.append(int(caracter))
        elif caracter == "x" and bandera:
            lista.append(10)
        else:
            return False
    
    if len(lista) != 10:
        return False
    
    lista2 = []
    num = 10
    for numero in lista:
        producto = numero * num
        lista2.append(producto)
        num -= 1
    
    return sum(lista2) % 11 == 0