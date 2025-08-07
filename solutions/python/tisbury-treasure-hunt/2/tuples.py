def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    tupla = tuple(azara_record[1])
    return tupla == rui_record[1]

def create_record(azara_record, rui_record):
    match = compare_records(azara_record,rui_record)
    if match:
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):
    resultado = []
    for tupla in combined_record_group:
        # Crear una nueva tupla sin el segundo elemento (índice 1)
        nueva_tupla = (tupla[0],) + tupla[2:]
        resultado.append(str(nueva_tupla))
    # Unir todos los registros con un salto de línea
    return "\n".join(resultado) + "\n"