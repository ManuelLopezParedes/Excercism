def is_armstrong_number(number):
    lista = list(map(int, str((number))))
    cantidad = len(lista)

    total = 0
    for numero in lista:
        suma = numero ** cantidad
        print(suma)
        total += suma
    if total == int(number):
        return True
    else:
        return False