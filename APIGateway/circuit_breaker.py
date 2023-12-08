number_of_tries = 0

def circuit_breaker():
    global number_of_tries
    number_of_tries += 1
    if number_of_tries > 4:
        return True
    else:
        return False