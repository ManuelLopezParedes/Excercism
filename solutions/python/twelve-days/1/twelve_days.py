def recite(start_verse, end_verse):
    # inicializacion de variables
    res = [] # resultado final
    verso_i = start_verse -1 # ajustamos los indices a base 0
    verso_f = end_verse -1

    # cuerpo del poema
    dias = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
    regalos = ["a Partridge in a Pear Tree.",
              "two Turtle Doves, ",
              "three French Hens, ",
              "four Calling Birds, ",
              "five Gold Rings, ",
              "six Geese-a-Laying, ",
              "seven Swans-a-Swimming, ",
              "eight Maids-a-Milking, ",
              "nine Ladies Dancing, ",
              "ten Lords-a-Leaping, ",
              "eleven Pipers Piping, ",
              "twelve Drummers Drumming, "
              ]

    while verso_i <= verso_f: # agregamos el numero de repeticiones a la cancion

        texto = "" # cadena auxiliar para guardar los versos
        lista = [] # lista auxiliar para guardar los regalos

        texto += (f"On the {dias[verso_i]} day of Christmas my true love gave to me: ")

        # agregamos los regalos en orden inverso
        for j in range(verso_i,-1,-1):
            lista.append(regalos[j])

        # si hay multiples regalos agregamos and al ultimo elemento
        if len(lista) > 1:
            lista[-1] = f"and {lista[-1]}"
        
        # juntamos los regalos en el texto y los agregamos a la lista final
        texto += "".join(lista)
        res.append(texto)
        verso_i += 1

    return res