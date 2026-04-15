def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0 or number < 1:
        return False

    d = 3
    while d * d <= number:
        if number % d == 0:
            return False
        d += 2

    return True


def longest_coherent_prime_subsequence(sequence: list[int]) -> list[int]:
    start = 0
    end = 0
    current_start = 0
    length = len(sequence)
    if length < 2:
        return sequence

    for i, number in enumerate(sequence):
        if is_prime(number):
            continue
        if  end - start >= i - current_start:
            current_start = i + 1
            continue
        start = current_start
        end = i
        current_start = i + 1

    if end - start < length - current_start:
        start = current_start
        end = length

    return sequence[start:end]


sequence = [1,3,5,7,11,9,3,4,1,3,5,7,11,13,17,15]