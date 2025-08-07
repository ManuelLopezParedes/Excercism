def get_rounds(number):
    lista = [number, number + 1, number + 2]
    return lista

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds
    
def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    promedio = (hand[0] + hand[-1]) / 2
    equal = card_average(hand)
    mitad = (len(hand) // 2)
    if promedio == equal or hand[mitad] == equal:
        return True
    return False


def average_even_is_average_odd(hand):
    odd = sum(hand[1::2]) / len(hand[1::2])
    even = sum(hand[::2]) / len(hand[::2])
    return odd == even


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
