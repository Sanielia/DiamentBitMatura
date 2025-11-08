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

def is_prime_cache(number: int, known_primes: list[int]) -> tuple[bool, list[int]]:
    highest_known_prime = max(known_primes) if known_primes else 1
    if number == 2 or number in known_primes:
        return True, known_primes
    # It is okay that sometimes there is check for number < 1, cuz Python won't even calculate it, cuz of how or works
    if number < 2 or number % 2 == 0 or number < highest_known_prime:
        return False, known_primes

    for n in known_primes:
        if number % n == 0:
            return False, known_primes

    d = highest_known_prime + 2

    while d ** d <= number:
        if number % d == 0:
            return False, known_primes

    known_primes.append(number)
    return True, known_primes