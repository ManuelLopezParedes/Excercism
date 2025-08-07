def distance(strand_a, strand_b):
    # nos aseguramos de que las listas sean iguales 
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    cuenta = 0
    
    # recorremos ambas listas buscando los elementos diferentes
    for a, b in zip(strand_a, strand_b):
        if a != b:
            cuenta += 1 # sumamos 1 a la cuenta 
    return cuenta