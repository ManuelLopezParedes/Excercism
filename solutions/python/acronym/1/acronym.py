import re
def abbreviate(words):
    # creamos nuestra regla para separar palabras cuando hay espacio y guion
    separadores = r"[ _\-]"
    # separamos la palabra 
    texto = re.split(separadores,words)

    # agregamos la primer letra de cada palabara
    acronimo = "".join([texto[0] for texto in texto if texto])

    # convertimos las palabras en mayusculas
    return acronimo.upper()
