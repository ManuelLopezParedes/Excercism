def convert(number):
    cadena = ""
    if number % 3 == 0:
        cadena += "Pling"
    if number % 5 == 0:
        cadena += "Plang"
    if number % 7 == 0:
        cadena += "Plong"
    return cadena if cadena else str(number)
