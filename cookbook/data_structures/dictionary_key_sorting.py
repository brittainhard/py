rows = [
   {"fname": "Brian", "lname": "Jones", "uid": 1003},
   {"fname": "David", "lname": "Beazley", "uid": 1002},
   {"fname": "John", "lname": "Cleese", "uid": 1001},
   {"fname": "Big", "lname": "Jones", "uid": 1004},
]

from operator import itemgetter

"""
Weird shit.

The operator module provices typical python stuff implemented in C. This can be
useful for performance reasons. It has all the typicla stuff. Running itemgetter
gets the attribute faster I guess?

Using timeit tells me that it is many times faster. You can do a number of
things like this.
"""

rows_by_fname = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))
print(rows_by_fname)
print(rows_by_uid)


"""Alternative using get"""
potato = sorted(rows, key=lambda k: k.get("uid"))
