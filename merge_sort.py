def merge_sort(array: list) -> list:
    length = len(array)
    if length > 2:
        index_of_division = length//2 if length % 2 == 0 else length//2 + 1
        first_fragment = merge_sort(array[:index_of_division])
        second_fragment = merge_sort(array[index_of_division:])
    else:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return array

    new_array = []
    for i, n in enumerate(first_fragment):
        while n > second_fragment[i]:
            pass

    return []
