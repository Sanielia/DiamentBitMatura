def subsequence_with_highest_product(sequence: list[int]) -> list[int]:
    subsequence = []
    if len(sequence) < 2:
        return sequence

    for number in sequence:
        if number > 0:
            subsequence.append(number)

    return subsequence

print(subsequence_with_highest_product([20,4,-15,34,-1,-1,1,4]))