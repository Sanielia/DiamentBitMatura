from string import ascii_lowercase

def are_anagrams(a: str, b: str) -> bool:
    len_a = len(a)
    if len_a != len(b):
        return False

    letters = {k: 0 for k in ascii_lowercase}
    for i in range(len_a):
        letters[a[i]] += 1
        letters[b[i]] -= 1

    return all(i == 0 for i in letters.values())


def longest_coherent_anagrams_sequence(sequence: list[str]) -> list[str]:
    start = 0
    end = 0
    current_start = 0
    length = len(sequence)
    if length < 2:
        return sequence

    last_word = sequence[0]
    for i, word in enumerate(sequence):
        if are_anagrams(last_word, word):
            last_word = word
            continue
        last_word = word
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

print(longest_coherent_anagrams_sequence(["ryba", "bary", "skibidi", "uwu", "ryba", "bary", "brya", "lol"]))