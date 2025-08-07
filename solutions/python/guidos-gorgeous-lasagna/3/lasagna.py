"""funciones para preparar lasgna"""
EXPECTED_BAKE_TIME=40

def bake_time_remaining(minutos):
    """
    tiempo restante de horneado   
    """
    res = EXPECTED_BAKE_TIME - minutos
    return res

def preparation_time_in_minutes(layers):
    """
    funcion para saber los minutos por capa
    """
    res = layers * 2
    return res
    
def elapsed_time_in_minutes(layers,elapsed_bake_time):
    """
    tiempo estimado de preparación
    """
    res = (layers * 2) + elapsed_bake_time
    return res