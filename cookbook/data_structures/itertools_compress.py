from itertools import compress

"""
This doesn't really seem all that useful.
"""

addresses = [
    "5142 N CLARK",
    "5148 N CLARK",
    "5800 E 58TH",
    "2122 N CLARK",
    "5645 N RAVENSWOOD",
    "1060 W ADDISON",
    "4801 N BROADWAY",
    "1039 W GRAINVILLE",
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]

cp = list(compress(addresses, more5))
