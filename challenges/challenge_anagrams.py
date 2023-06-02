def compare(left, right):
    if not right:
        return left
    if not left:
        return right
    if right[0] < left[0]:
        return right[0] + compare(left, right[1:])
    else:
        return left[0] + compare(left[1:], right)


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    x = merge_sort(first_string.lower())
    z = merge_sort(second_string.lower())
    return (x, z, x == z)


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return compare(left, right)
