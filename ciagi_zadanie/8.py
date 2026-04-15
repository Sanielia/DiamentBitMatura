from string import ascii_lowercase

def have_same_number_of_ones_in_binary(a: int, b: int) -> bool:
    a_bin = str(bin(a))
    b_bin = str(bin(b))
    len_a_bin = len(a_bin)
    len_b_bin = len(b_bin)
    smaller = b_bin
    smaller_length = len_b_bin
    longer = a_bin
    length = len_a_bin
    if len_b_bin > len_a_bin:
        smaller = a_bin
        smaller_length = len_a_bin
        longer = b_bin
        length = len_b_bin

    count = 0
    for i in range(length):
        if i < smaller_length:
            if smaller[i] == "1":
                count -= 1
        if longer[i] == "1":
            count += 1

    return count == 0


def longest_coherent_sequence_with_same_number_of_ones_in_binary(sequence: list[int]) -> list[int]:
    start = 0
    end = 0
    current_start = 0
    length = len(sequence)
    if length < 2:
        return sequence

    last_number = sequence[0]
    for i, number in enumerate(sequence):
        if have_same_number_of_ones_in_binary(last_number, number):
            last_number = number
            continue
        last_number = number
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

print(longest_coherent_sequence_with_same_number_of_ones_in_binary([1, 2, 4, 3, 0, 3, 5, 6, 9, 8]))