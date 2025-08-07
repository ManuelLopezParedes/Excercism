def answer(question):
    limpio = question.replace("?","") # limpiamos la lista quitando "?"
    pregunta = limpio.split()
    valido = " ".join(pregunta[:2:]) # extraemos los dos primeros elementos
    res = 0 # resultado total
    operacion=[] # lista para ir agregando operaciones

    # evaluamos si la pregunta es correcta
    if valido != "What is":
        raise ValueError("syntax error")
    if len(pregunta) == 3:
        return int(pregunta[-1])

    # ignoramos los 2 primeros elementos
    for palabra in pregunta[2::]:
        # evaluar si es numero
        try:
            numero = int(palabra)
            operacion.append(numero) # agregamos el numero a la lista
        # si no es numero  evaluamos si es operacion
        except(ValueError):
            if palabra == "plus":
                operacion.append("+") # convertimos plus a +
            elif palabra == "minus":
                operacion.append("-") # convertimos minus a -
            elif palabra == "multiplied":
                operacion.append("*") # convertimos multiplied a *
            elif palabra == "divided":
                operacion.append("/") # convertimos divided a /
            else:
                if palabra == "by": # agregamos una excepcion a by ya que va en conjunto a multiplied y divided
                    continue
                else: # si no es ninguna regresamos un value error  
                    raise ValueError("unknown operation")
                
        # si la operación tiene 3 elementos
        if len(operacion) == 3:
            try:
                if isinstance(operacion[0],(int,float)):
                    res = eval("".join(str(e) for e in operacion)) # usamos eval para resolver la operacion
                    operacion.clear() # limpiamos la lista
                    operacion.append(res) # agregamos el resultado por si hay mas operaciones
                else:
                    raise ValueError("syntax error")
            except Exception: # si la operacion no se pueede resolver regresamos un ValueError
                raise ValueError("syntax error")
    
    # si la lista tiene 0 o mas de 1 elemento manda un error
    if len(operacion) != 1:
        raise ValueError("syntax error")
    return res