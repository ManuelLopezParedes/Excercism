def value_of_card(card):
    if card in {'K','Q','J'}:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    a = value_of_card(card_one)
    b = value_of_card(card_two)
    if a == 1:
        a = value_of_ace(a,b)
    elif b == 1:
        b = value_of_ace(b,a)

    if a > b:
        return card_one
    elif b > a:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    a = value_of_card(card_one)
    b = value_of_card(card_two)
    if a == 1 or b == 1 or (a + b + 11 > 21):
        return 1 
    else:
        return 11

def is_blackjack(card_one, card_two):
    a = value_of_card(card_one)
    b = value_of_card(card_two)

    return (a == 1 and b == 10) or (a == 10 and b == 1)

def can_split_pairs(card_one, card_two):
    a = value_of_card(card_one)
    b = value_of_card(card_two)
    return a == b


def can_double_down(card_one, card_two):
    a = value_of_card(card_one)
    b = value_of_card(card_two)
    return (a + b) in {9,10,11}
