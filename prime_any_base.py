from natural_conversion import convert_to_decimal
from prime_factorization import is_prime


def is_prime_with_base(number: str, base: int) -> bool:
    number = convert_to_decimal(number, base)
    return is_prime(number)


if __name__ == "__main__":
    print(is_prime_with_base("D", 16))
