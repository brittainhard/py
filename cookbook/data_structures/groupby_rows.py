"""
Groupby takes a key argument to determine what dictionary item to sory by.

There is a serious limitation though. If the items arent sorted beforehand the
groupy breaks down and gives you a weird set of things.
"""

from itertools import groupby
from operator import itemgetter


rows = [
    {"address": "5142 N CLARK", "date": "07/1/2012"},
    {"address": "5148 N CLARK", "date": "07/4/2012"},
    {"address": "5800 E 58TH", "date": "07/2/2012"},
    {"address": "2122 N CLARK", "date": "07/3/2012"},
    {"address": "5645 N RAVENSWOOD", "date": "07/2/2012"},
    {"address": "1060 W ADDISON", "date": "07/2/2012"},
    {"address": "4801 N BROADWAY", "date": "07/1/2012"},
    {"address": "1039 W GRAINVILLE", "date": "07/4/2012"}
]

# Sort by the desired field
rows.sort(key=itemgetter("date"))

# Iterate in groups.
for date, items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print("    ", i)
