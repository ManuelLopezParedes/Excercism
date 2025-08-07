def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    eficiencia = ((voltage * current)/theoretical_max_power)*100 # eficiencia del reactor
    # si la eficienca es mayor al 80 regresamos verde
    if eficiencia >= 80:
        return "green"
    # si la eficiencia es mayor o igual a 60 regresamos naranja
    elif eficiencia >= 60:
        return "orange"
    # si la eficiencia es mayor o igual a 30 regreamos rojo
    elif eficiencia >= 30:
        return "red"
    # si la eficiencia es menor a 30 regresamos negro
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # calculamos el rango 
    rango = temperature * neutrons_produced_per_second
    # si el rango es menos al 90% del limite regresamos low
    if rango < ((threshold * 90)/100):
        return 'LOW'
    # si el rango se encuentra entre el -10% y +10% del rango regresamos normal 
    elif rango < (threshold * .10) + threshold and rango > (threshold * .10) - threshold:
        return 'NORMAL'
    # si no se cumple ninguna regresamos danger
    else:
        return 'DANGER'