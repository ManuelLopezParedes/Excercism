def square(number):
    if number < 1 or  number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        granos = 2 ** (number - 1)
        print(granos)
    return granos


def total():
    total= (2 ** 64) - 1
    return total
