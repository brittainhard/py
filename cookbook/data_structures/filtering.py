from functools import partial

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5. -6, -7, -8]


a = partial(lambda: [n for n in sample_list if n > 0])
b = partial(lambda: (n for n in sample_list if n > 0))

"""
Sometimes it is necessary to express the filter criteria in a function.
"""
values = ["1", "2", "-3", "-", "4", "N/A", "5"]


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)
