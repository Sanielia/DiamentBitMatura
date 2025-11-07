def merge_sort(array: list) -> list:
    length = len(array)
    if length > 2:
        index_of_division = length//2 if length % 2 == 0 else length//2 + 1
        first_fragment = merge_sort(array[:index_of_division])
        second_fragment = merge_sort(array[index_of_division:])
    else:
        if length == 2 and array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array

    new_array = []
    for num in first_fragment:
        while len(second_fragment) > 0 and num > second_fragment[0]:
            new_array.append(second_fragment[0])
            del second_fragment[0]
        else:
            new_array.append(num)

    if len(second_fragment) > 0:
        new_array += second_fragment
    return new_array


if __name__ == "__main__":
    print(merge_sort([5, 4, 3, 2, 1]))
    print(merge_sort([10, 8, 9, 6, 7]))
    print(merge_sort([21, 42, 37]))
    print(merge_sort([2, 1, 3, 7, 4, 2, 0, 6, 9]))
