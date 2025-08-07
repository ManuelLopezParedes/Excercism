def reverse(text):
    i = 1
    lista = []
    for char in text:
        lista.append(text[-i])
        i += 1
    return ''.join(lista)