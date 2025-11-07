def gcd(a: int, b: int) -> int:
    d = 2
    gcd = 1
    while d <= min(a, b) > 1:
        while a % d == 0 and b % d == 0:
            gcd *= d
            a, b = a // d, b // d
        d += 1 if d == 2 else 2

    return gcd


def gcd_euclidean(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd_euclidean(a, b)

if __name__ == "__main__":
    print(gcd_euclidean(88, 2133112))
