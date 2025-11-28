def exercise3(table: list[list[int]]) -> None:
    [print(sum(row)/len(row)) for row in table]


def exercise4(power_table: list[list[int]]) -> int:
    count = 0
    for y in range(1, len(power_table) - 1):
        for x in range(1, len(power_table[y]) - 1):
            neighbours = [power_table[y+1][x], power_table[y-1][x], power_table[y][x-1], power_table[y-1][x]]
            power = power_table[y][x]
            if power > max(neighbours):
                count += 1
    return count



if __name__ == "__main__":
    exercise3([[5, 242, 411], [433, 5, 1], [5325, 555, 1121213123], [1, 2, 3]])
    print(exercise4([
        [1, 2, 5, 2, 1],
        [1, 3, 6, 3, 1],
        [1, 4, 3, 3, 1],
        [1, 2, 5, 4, 1],
        [1, 2, 4, 2, 1]
    ]))
