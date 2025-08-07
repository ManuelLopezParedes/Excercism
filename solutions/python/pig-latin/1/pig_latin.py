def translate_word(word):
    vocales = ['a', 'e', 'i', 'o', 'u']
    consonantes = []

    # Regla 1: Comienza con vocal, "xr" o "yt"
    if word[0] in vocales or word[:2] in ["xr", "yt"]:
        return word + "ay"

    # Regla 2, 3 y 4: Comienza con consonantes
    i = 0
    while i < len(word):
        # Manejo de "qu" (Regla 3)
        if word[i:i+2] == "qu":
            consonantes.append(word[i:i+2])
            i += 2
            break  # Salimos del bucle después de manejar "qu"
        # Manejo de "y" (Regla 4)
        elif word[i] == 'y' and i != 0:  # "y" no se trata como vocal al principio
            break
        # Manejo de consonantes normales (Regla 2)
        elif word[i] not in vocales:
            consonantes.append(word[i])
            i += 1
        else:
            break  # Salimos del bucle si encontramos una vocal

    # Construye la nueva cadena
    nueva_cadena = word[i:] + "".join(consonantes) + "ay"
    return nueva_cadena

def translate(text):
    # Divide la oración en palabras, traduce cada palabra y las une de nuevo
    palabras = text.split(" ")
    palabras_traducidas = [translate_word(palabra) for palabra in palabras]
    return " ".join(palabras_traducidas)