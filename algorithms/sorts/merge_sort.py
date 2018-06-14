import random


def merge_sort(array):
    first = array[len(array) // 2:]
    second = array[:len(array) // 2]
    combined = []
    if len(array) > 2:
        first = merge_sort(first)
        second = merge_sort(second)
    if len(first) + len(second) == 1:
        return first + second
    while bool(first) and bool(second):
        if first[0] < second[0]:
            combined.append(first.pop(0))
        elif first[0] > second[0]:
            combined.append(second.pop(0))
        elif first[0] == second[0]:
            combined.append(first.pop(0))
    if bool(first):
        combined += first
    elif bool(second):
        combined += second
    return combined
