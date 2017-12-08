import re


line = "asdf fjdk; afed, fjek,asdf, foo"
a = re.split(r"[;,\s]\s*", line)

# Using a capture group in parentheses. The thing here is that it will split
# based on these things, but it will also include those split characters in the
# split.
fields = re.split(r"(;|,|\s)\s*", line)

values = fields[::2]
delimiters = fields[1::2] + ['']

rejoin = ''.join(v + d for v, d in zip(values, delimiters))

print(delimiters)
print(values)


print(line)
print(rejoin)
