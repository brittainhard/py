a = {
    "x": 1,
    "y": 2,
    "z": 3
}

b = {
    "w": 10,
    "x": 11,
    "y": 2
}

print("In a and b")
print(a.keys() & b.keys())
print("In a but not in b")
print(a.keys() - b.keys())
print(a.items() & b.items())

print("Make a new dictionary with certain keys removed.")
c = {key: a[key] for key in a.keys() - {"z", "w"}}
print(c)
