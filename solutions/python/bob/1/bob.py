def response(hey_bob):
    cadena = hey_bob.strip()
    if len(cadena) == 0:
        return "Fine. Be that way!"
    else:
        lista =list(cadena)

        if cadena.isupper() and lista[-1] == '?':
            return "Calm down, I know what I'm doing!"
        elif not cadena.isupper() and lista[-1] == '?':
            return "Sure."
        elif cadena.isupper():
            return "Whoa, chill out!"
        else:
            return "Whatever."
    