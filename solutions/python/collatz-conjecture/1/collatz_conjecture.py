def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        pasos=0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                pasos +=1
            else:
                number = (number * 3) + 1
                pasos +=1
    return pasos
