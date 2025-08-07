def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        i = 1
        lista = []
        while i < number:
            if number % i == 0:
                lista.append(i)
            i += 1
        if sum(lista) == number:
            return "perfect"
        elif sum(lista) < number:
            return "deficient"
        else:
            return "abundant"