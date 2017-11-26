from collections import ChainMap


"""
If you delete an item from a dictionary, it always deletes it from the latest
dictionary.

This will make those dictionaries incongruent.
"""
a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
c = ChainMap(a, b)
del c["z"]
print(c)


"""
Scoped variables?

Lets you keep a dict that has a chain of variables, kind of like a stack.
"""
values = ChainMap()
values["x"] = 1
values = values.new_child()
values["x"] = 2
values = values.new_child()
values["x"] = 3
print(values["x"])
print(values)
print(values.parents["x"])
print(values.parents)
print(values.parents.parents["x"])
print(values.parents.parents)


"""
If you use dictionary update to combine multiple dictionaries, it creates a new
copy. With chainmap you can keep copies of all the dictionaries.
"""
d = dict(b)
d.update(a)
print(d)
