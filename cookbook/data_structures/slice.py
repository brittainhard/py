potato = "This is a potato"
a = potato[10:]
print(a)

"""
So pythonic, so functiononic."

Get the last part of the string, ending point is none, so it just goes to the
end of the string.
"""
b = slice(10, None)
print(potato[b])

