def better_int(digit: str) -> int:
    try:
        return int(digit)
    except ValueError:
        return ord(digit.upper()) - ord('A') + 10


def convert_to_decimal(number: str, base: int) -> int:
    result = 0
    for i, digit in enumerate(reversed(number)):
        result += better_int(digit) * (base ** i)

    return result

# Proszę napisać funkcję, który przyjmuje dwie liczby w systemie pozycyjnym p
# (3 argumenty: liczba 1, liczba 2, podstawa systemu p) i zwraca ich sumę (w dowolnym systemie).
def sum_with_given_base(first_number: str, second_number: str, base: int) -> int:
    return convert_to_decimal(first_number, base) + convert_to_decimal(second_number, base)


def prime_factorization(number) -> list[int]:
    d = 2
    prime_factors = []
    while number > 1:
        while number % d == 0:
            prime_factors.append(d)
            number//=d
        d = d + 2 if d > 2 else 3

    return prime_factors

# Proszę napisać funkcję sprawdzającą, czy suma cyfr podanej liczby jest
# większa od sumy jej unikatowych czynników pierwszych.
def is_digit_sum_greater_than_unique_prime_factors_sum(number) -> bool:
    unique_prime_factors = set(prime_factorization(number))
    prime_factors_sum = sum(unique_prime_factors)
    digits_sum = sum([int(ch) for ch in str(number)])

    return digits_sum > prime_factors_sum