"""Functions to automate Conda airlines ticketing system."""


from shlex import join


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    lista = ["A","B","C","D"]
    j = 0
    for i in range(number):
        if j == 4:
            j = 0
        yield lista[j]
        j += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    generador = generate_seat_letters(number)
    fila  = 1
    
    for i in range(number):
        siguiente = next(generador)
        yield f"{fila}{siguiente}"

        if siguiente == "D":
            fila += 1
            if fila == 13:
                fila = 14

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    pasajeros = {}
    asiento = generate_seats(len(passengers))

    for item in passengers:
        pasajeros[item] = next(asiento)
    return pasajeros

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for item in seat_numbers:
        res = f"{item}{flight_id}"
        while len(res) < 12:
            res = res + "0"
        yield res