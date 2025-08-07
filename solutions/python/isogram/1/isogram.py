def is_isogram(string):
    palabra = string.lower()
    cadena_filtrada = palabra.replace("-", "").replace(" ","")
    return len(set(cadena_filtrada)) == len(cadena_filtrada)
