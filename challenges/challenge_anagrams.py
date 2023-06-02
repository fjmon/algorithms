def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[:mid])
    return combine(left, right)


def combine(left, right):
    if not right:
        return left
    if not left:
        return right
    if right[0] < left[0]:
        return right[0] + combine(left, right[1:])
    else:
        return left[0] + combine(left[1:], right)


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    first_string = merge_sort(list(first_string.lower()))
    second_string = merge_sort(list(second_string.lower()))

    x = ''.join(first_string)
    y = ''.join(second_string)
    return (x, y, x == y)
