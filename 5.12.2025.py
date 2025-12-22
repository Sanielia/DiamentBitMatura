def are_similar(a: list[int], b: list[int], k: int):
    return a[0:k] == b[len(b)-k:] and b[0:len(b)-k] == a[k:]


def test_are_similar():
    a = [4, 7, 1, 4, 5]
    b = [1, 4, 5, 4, 7]
    assert are_similar(a, b, 2)


if __name__ == "__main__":
    test_are_similar()