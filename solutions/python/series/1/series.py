def slices(series, length):
    ser = str(series)
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif not series:
        raise ValueError("series cannot be empty")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    else:
        lista = []
        cadena = ""
        for i in range(len(ser) - length + 1):
            cadena += ser[i:i+length] 
            lista.append(cadena)
            cadena = ""
    return lista
