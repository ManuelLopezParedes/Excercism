def resistor_label(colors):
    esquema = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    resistencia = {"grey" : " ±0.05%", "violet" : " ±0.1%", "blue" : " ±0.25%", "green" : " ±0.5%", "brown" : " ±1%", "red" : " ±2%", "gold" : " ±5%", "silver" : " ±10%"}
    
    # Manejar caso especial de resistencia de 0 ohms
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    
    # Calcular el valor de la resistencia
    if len(colors) == 4:
        r = ((esquema.index(colors[0]) * 10) + esquema.index(colors[1])) * (10 ** esquema.index(colors[2]))
    else:
        r = (((esquema.index(colors[0]) * 100) + (esquema.index(colors[1]) * 10) + esquema.index(colors[2])) * (10 ** esquema.index(colors[3])))

    # Formatear el valor con las unidades apropiadas
    if r < 1000:
        value = r
        unit = "ohms"
    elif r < 1000000:
        value = r / 1000
        unit = "kiloohms"
    elif r < 1000000000:
        value = r / 1000000
        unit = "megaohms"
    else:
        value = r / 1000000000
        unit = "gigaohms"
    
    # Formatear el valor para eliminar .0 si es entero
    if value == int(value):
        value_str = str(int(value))
    else:
        value_str = str(value)
    
    result = f"{value_str} {unit}"

    if colors[-1] in resistencia:
        result += resistencia[colors[-1]]

    return result