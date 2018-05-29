import random


def bubble_sort(items):
    for y in range(len(items)):
        for x in range(0, len(items)):
            a = items[x]
            if x == len(items) - 1:
                break
            b = items[x + 1]
            if a > b:
                items[x] = b
                items[x + 1] = a
    return items


a = [x for x in range(100)]
print(a)
