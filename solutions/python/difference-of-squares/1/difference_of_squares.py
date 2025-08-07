def square_of_sum(number):
    i = 0
    res = 0
    while i <= number:
        res += i
        i += 1
    return res ** 2
    
def sum_of_squares(number):
    i = 0
    res = 0
    while i <= number:
        res += (i ** 2)
        i += 1
    return res

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)