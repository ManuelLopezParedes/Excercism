# creamos nuestro diccionario
code = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"}
def encode(plain_text):
    lista = decode(plain_text) #codificamos el texto

    texto = []
    for i in range(0, len(lista), 5):  # Recorremos la cadena en pasos de 5
        texto.append("".join(lista[i:i+5]))
        texto.append(" ")  # Agregamos un espacio después de cada bloque
    
    if texto[-1] == " ":  # Eliminamos el espacio extra al final
        texto.pop()
    return "".join(texto)

def decode(ciphered_text):
    lista =[]
    texto = ciphered_text.replace(" ","") # quitamos los espacios del texto
    for item in texto:
        if item in ".,": #saltamos puntos y comas 
            continue
        elif item.lower() in code:
            lista.append(code[item.lower()]) # agregamos el elemento codificafo
        else:
            lista.append(item) # agregamos elementos que no se pueden codificar
    return "".join(lista)