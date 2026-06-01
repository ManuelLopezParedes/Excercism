def prime(numero):
    if numero < 1:
        raise ValueError('there is no zeroth prime')
    
    contador = 0
    actual = 1

    while contador < numero:
        actual += 1
        primo = True
        limite = int(actual **0.5) + 1

        for i in range(2, limite):
            if actual % i == 0:
                primo = False
                break

        if primo:
            contador +=1

    return actual

