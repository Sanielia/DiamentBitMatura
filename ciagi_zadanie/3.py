def coherent_subsequence_with_highest_product(sequence: list[int]) -> list[int]:
    highest_product = 0
    best_subsequence = []
    length = len(sequence)
    if length < 2:
        return sequence

    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence) + 1):
            sub_sequence = sequence[i:j]
            product = calculate_product(sub_sequence)
            if highest_product < product:
                best_subsequence = sub_sequence
                highest_product = product

    return best_subsequence


def calculate_product(sequence: list[int]) -> int:
    product = 1
    for number in sequence:
        product *= number
    return product