def longest_not_descending_coherent_subsequence(sequence: list[int]) -> list[int]:
    start = 0
    end = 0
    current_start = 0
    length = len(sequence)
    if length < 2:
        return sequence

    last_number = sequence[0]

    for i, number in enumerate(sequence):
        if number >= last_number:
            last_number = number
            continue
        last_number = number
        if  end - start >= i - current_start:
            current_start = i
            continue
        start = current_start
        end = i
        current_start = i

    if end - start < length - current_start:
        start = current_start
        end = length

    return sequence[start:end]

for arr in [[1, 2, 2, 1, 3, 4],
[5, 4, 3, 2, 1],
[1, 3, 2, 2, 5, 6],
[-3, -2, -2, -1],
[1, 2, 3, 0, 1, 2]]:
    print(longest_not_descending_coherent_subsequence(arr))