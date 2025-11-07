def better_int(digit: str) -> int:
    if not digit.isalnum():
        raise ValueError(f"{digit} cannot be converted to integer")
    try:
        return int(digit)
    except ValueError:
        return ord(digit.upper()) - ord('A') + 10


def convert_to_decimal(number: str, base: int) -> int:
    result = 0
    for i, digit in enumerate(reversed(number)):
        result += better_int(digit) * (base ** i)

    return result


def handle_higher_digits(number: int) -> str:
    if number < 10:
        return str(number)
    return chr(number + ord('A') - 10)


def convert_from_decimal(number: int, base: int) -> str:
    result = ""
    while number != 0:
        result += handle_higher_digits(number % base)
        number //= base
    return result[::-1]

if __name__ == "__main__":
    while True:
        number = int(input("give number to convert "))
        # number = input("give number to convert ")
        base = int(input("give target base "))
        print(convert_from_decimal(number, base))