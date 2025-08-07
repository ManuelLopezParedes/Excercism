def decode(string):
    cadena = ""
    num = ""
    for item in string:
        if item.isdigit():
            num += item
        else:
            if not num:
                cadena += item
            else:
                cadena += item * int(num)
                num = ""
    return cadena


def encode(string):
    cadena = ""
    num = 0
    eval = ""
    if not string:
        return cadena
    for item in string:
        if not eval:
            eval = item
            num += 1
        else:
            if item == eval:
                num += 1
            else:
                if num == 1:
                    cadena += eval
                else:
                    cadena += str(num) + eval
                num = 1
                eval = item
    if num == 1:
        cadena += eval
    else:
        cadena += str(num) + eval
    return cadena