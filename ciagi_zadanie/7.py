from math import gcd


def longest_coherent_non_coprime_sequence(sequence: list[int]) -> list[int]:
    start = 0
    end = 0
    current_start = 0
    length = len(sequence)
    last_gcd = sequence[0]
    if length < 2:
        return sequence

    for i, number in enumerate(sequence):
        current_gcd = gcd(last_gcd, number)
        if current_gcd > 1:
            last_gcd = current_gcd
            continue
        last_gcd = number
        if end - start >= i - current_start:
            current_start = i
            continue
        start = current_start
        end = i
        current_start = i

    if end - start < length - current_start:
        start = current_start
        end = length

    return sequence[start:end]

print(longest_coherent_non_coprime_sequence([2, 4, 6, 5, 5, 6, 9, 12, 33, 4]))