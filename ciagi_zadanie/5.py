from typing import Generator


def longest_increasing_subsequence(sequence: list[int]) -> list[int]:
    length = len(sequence)
    if length < 2:
        return sequence

    for i in range(length, 1, -1):
        for subsequence in combinations(sequence, i):
            ok = True
            last_number = subsequence[0]
            for number in subsequence[1:]:
                if number <= last_number:
                    ok = False
                    break
                last_number = number

            if ok:
                return subsequence

    return [sequence[0]]

def combinations(sequence: list[int], subsequence_length: int) -> Generator[list[int]]:
    freezed_sequence = tuple(sequence)
    length = len(freezed_sequence)

    if subsequence_length > length:
        yield []
        return

    indexes = list(range(subsequence_length))
    yield [freezed_sequence[i] for i in indexes]

    while True:
        for i in reversed(range(subsequence_length)):
            if indexes[i] != i + length - subsequence_length:
                break
        else:
            return

        indexes[i] += 1
        for j in range(i + 1, subsequence_length):
            indexes[j] = indexes[j - 1] + 1

        yield [freezed_sequence[i] for i in indexes]


print(longest_increasing_subsequence([1,2,3,4,0,-1,5,7,8,-3,9,8,7,6,5,4,3,2,1,-1,-2,-3]))