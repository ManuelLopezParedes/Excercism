def square_root(number):
    low = 0
    high = number
    
    while low <= high:
        mitad = (low + high) // 2
        square = mitad * mitad
        
        if square == number:
            return mitad
        elif square < number:
            low = mitad + 1
        else:
            high = mitad - 1
