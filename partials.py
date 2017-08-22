from functools import partial

"""
Some notes about how partial functions work.

They are lazy evaluation. 
"""
class Potato:

    def __init__(self, a, b):
        self.a = a
        self.b = b


# Combine the class with all of the arguments you need to supply to it. When you
# call the function, it applies the arguments to the function, or the class in
# this case.

part_class = partial(Potato, 1, 2)
print(part_class)
a = part_class()
print(a.a)
