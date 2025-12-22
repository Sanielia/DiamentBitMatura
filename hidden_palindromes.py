import sys


def is_palindrome(text: str) -> bool:
    for i in range(len(text) // 2):
        if text[i] != text[-i-1]:
            return False

    return True

def test_is_palindrome():
    assert is_palindrome("kajak")
    assert not is_palindrome("python")
    assert is_palindrome("kamilslimak")


def find_inner_palindromes(text: str) -> set[str]:
    palindromes: set[str] = set()
    inner_palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            if is_palindrome(text[i:j]):
                palindromes.add(text[i:j])

    for p in palindromes:
        for q in palindromes:
            if p != q and p in q:
                inner_palindromes.add(p)

    return inner_palindromes

def test_find_inner_palindromes():
    assert find_inner_palindromes("kajak") == {"aja", "j", "k", "a"}
    assert find_inner_palindromes("kamilslimak") == {"amilslima", "milslim", "ilsli", "lsl", "s", "k", "a", "m", "i", "l"}
    assert find_inner_palindromes("kamilslimakajak") == {"amilslima", "milslim", "ilsli", "lsl", "s", "k", "a", "m", "i", "l", "aja", "j"}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            test_is_palindrome()
            print("Test is_palindrome passed!")
            test_find_inner_palindromes()
            print("Test find_inner_palindromes passed!")