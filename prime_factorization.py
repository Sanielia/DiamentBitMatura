def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0 or number < 1:
        return False

    d = 3
    while d * d < number:
        if number % d == 0:
            return False
        d += 2

    return True