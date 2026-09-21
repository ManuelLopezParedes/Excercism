def count_words(sentence):
    contador = {}
    # convertimos mayusculas en minusculas
    sentence = sentence.lower()
    # remplasamos los caracteres con espacios
    sentence = sentence.replace(","," ").replace("."," ").replace("_"," ")
    # separamos la sentencia en palabras
    sentence = sentence.split()
    for item in sentence:
        # limpiamos la palabra de caracteres especiales
        palabra_limpia = item.strip("':.!&@$%^&")
        if palabra_limpia:
            # regresamos el valor, si no existe lo inicializa en 0 y le suma 1
            contador[palabra_limpia] = contador.get(palabra_limpia,0) + 1
    return contador