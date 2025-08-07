def is_paired(input_string):
    stack = []  # Usamos una pila para rastrear los caracteres de apertura
    matching_pairs = {")": "(", "]": "[", "}": "{"}

    for char in input_string:
        if char in "([{":  # Si es un carácter de apertura
            stack.append(char)
        elif char in ")]}":  # Si es un carácter de cierre
            # Verifica si hay un par que coincida
            if stack and stack[-1] == matching_pairs[char]:
                stack.pop()  # Elimina el carácter coincidente de la pila
            else:
                return False  # Si no coincide, no está balanceado

    # Si la pila está vacía, todos los caracteres están balanceados
    return not stack
