from natural_conversion import handle_higher_digits

def decimal_to_binary(number: int) -> str:
    result = ""
    is_positive = True if number >= 0 else False
    if not is_positive:
        number = number * -1
    while number != 0:
        result += handle_higher_digits(number % 2)
        number //= 2
    if is_positive:
        return result[::-1]
    if len(result) < 8:
        result = "0" * (8 - len(result)) + result
    converted_result = ""
    for digit in reversed(result):
        match digit:
            case "0":
                converted_result += "1"
            case "1":
                converted_result += "0"
    converted_result += "1"
    return converted_result

if __name__ == "__main__":
    print(decimal_to_binary(-120))