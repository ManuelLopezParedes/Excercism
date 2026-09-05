def line_up(name, number):
    digito = number % 10
    dos_digitos =number % 100
    if digito == 1 and dos_digitos != 11:
        terminacion = "st"
    elif digito == 2 and dos_digitos !=12:
        terminacion = "nd"
    elif digito == 3 and dos_digitos !=13:
        terminacion = "rd"
    else:
        terminacion = "th"

    return f"{name}, you are the {number}{terminacion} customer we serve today. Thank you!"