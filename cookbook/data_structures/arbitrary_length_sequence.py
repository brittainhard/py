import numpy as np

def drop_first_last(grades):
    first, *middle, last = grades
    assert type(middle) == list
    return np.mean(middle)

record = ("Dave", "dave@example.com", "773-552-1212", "847-555-1212")

name, email, *phone_numbers = record

"""Unpacking tuples."""

records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3, 4)
]

def do_foo(x, y):
    print("foo", x, y)

def do_bar(s):
    print("bar", s)

for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)

print("\n")

"""String splitting with arbitrary length sequences."""

line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"

uname, *fields, homedir, sh = line.split(":")
print(uname)
print(fields)
print(homedir)
print(sh)
print("\n")

"""Throwaway variables."""
record = ("ACME", 50, 123.45, (12, 18, 2012))
name, *_, (*_, year), = record
print(name)
print(year)
print("\n")

"""This list processing is like functional languages."""

items = [1, 2, 3, 4, 5]
head, *tail = items
print(head)
print(tail)
print("\n")

"""Recursive sum algorithm."""

def sum_new(items):
    head, *tail = items
    return head + sum_new(tail) if tail else head

print(sum_new([1, 2, 3, 4, 5]))
