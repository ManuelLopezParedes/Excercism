def say(number):
    # manejo de excepciones 
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    # diccionario con su cardinal
    unidades= { 1:"one",
                2:"two",
                3:"three",
                4:"four",
                5:"five",
                6:"six",
                7:"seven",
                8:"eight",
                9:"nine",
                10:"ten",
                11:"eleven",
                12:"twelve",
                13:"thirteen",
                14:"fourteen",
                15:"fifteen",
                16:"sixteen",
                17:"seventeen",
                18:"eighteen",
                19:"nineteen"}
    
    # diccionario con decenas y su cardinal
    decenas = {20:"twenty",
               30:"thirty",
               40:"forty",
               50:"fifty",
               60:"sixty",
               70:"seventy",
               80:"eighty",
               90:"ninety",}

    # variables de control
    prefijo = ["", " thousand", " million", " billion"]
    contador = 0
    palabra = ""

    while number > 0:
        tmp_palabra = ""
        
        # separamos el numero en centenas y decenas_unidades 
        tmp = number % 1000
        centenas = tmp // 100
        decenas_unidades = tmp % 100

        # convertimos las centanas en palabra
        if centenas > 0:
            tmp_palabra = unidades[centenas] + " hundred"

        # convertimos las decenas y unidades
        if decenas_unidades >= 20:
            # si es mayor o igual a 20 separamos en decenas y unidades
            tmp_decenas = (decenas_unidades // 10) * 10
            tmp_unidades = decenas_unidades % 10
            # si no hay unidades solo agregamos las decenas
            if tmp_unidades == 0:
                tmp_palabra = tmp_palabra + " " + decenas[tmp_decenas]
            # unimos decenas y unidades con un "-"
            else:
                tmp_palabra = tmp_palabra + " " + decenas[tmp_decenas] + "-" + unidades[tmp_unidades]
        # si es menor a 20
        else:
            if decenas_unidades > 0: # nos aseguramos que haya unidades 
                tmp_palabra = tmp_palabra + unidades[decenas_unidades]

        # nos aseguramos que tengamos numero para evitar agregar solo el sufijo
        if tmp > 0: 
            tmp_palabra = tmp_palabra + prefijo[contador]

        palabra = tmp_palabra + " " + palabra
        contador += 1   
        number = number // 1000

    return palabra.strip() # damos formato a nuestro texto
