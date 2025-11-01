def bubble_sort(array: list) -> list:
    new_array = [array[0]]
    last_item = array[0]
    for i, item in enumerate(array[1:]):
        if last_item > item:
            new_array[i - 1] = item
            new_array.append(last_item)
        else:
            new_array.append(last_item)
        last_item = item

    if array != new_array:
        new_array = bubble_sort(new_array)
    return new_array