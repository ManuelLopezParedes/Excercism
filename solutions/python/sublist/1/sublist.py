# Possible sublist categories.
# Change the values as you see fit.
# Definimos las constantes
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    # Verificamos si las listas son iguales
    if list_one == list_two:
        return EQUAL
    
    # Verificamos si list_one es una sublista de list_two
    if is_sublist(list_one, list_two):
        return SUBLIST
    
    # Verificamos si list_two es una sublista de list_one
    if is_sublist(list_two, list_one):
        return SUPERLIST
    
    # Si no se cumple ninguna de las condiciones anteriores, las listas son desiguales
    return UNEQUAL

def is_sublist(smaller, larger):
    #Verifica si `smaller` es una sublista de `larger`.
    len_smaller = len(smaller)
    len_larger = len(larger)
    
    # Si la lista más pequeña está vacía, es sublista de cualquier lista
    if len_smaller == 0:
        return True
    
    # Recorremos la lista más grande para verificar si la más pequeña está contenida
    for i in range(len_larger - len_smaller + 1):
        if larger[i:i + len_smaller] == smaller:
            return True
    
    return False
            
