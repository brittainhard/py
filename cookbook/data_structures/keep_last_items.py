"""
Deque is double-ended-queue. Lets you append and prepend to a list. Faster at
finding stuff I guess?

It is O(1) of memory use when inserting or popping, but lists are O(N).
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open("potato.txt") as f:
    for line, prevlines in search(f, "python", 3):
        for pline in prevlines:
            print(pline, end="")
        print(line, end="")
        print("-" * 20)


"""
You don't have to delete items from a deque. They are automatically deleted if
you add more items than the maxlength allows.

You can just use deques as lists too.
"""
p = deque(maxlen=3)
p.append(1)
p.append(2)
p.append(3)
p.append(4)
print(p)
p.appendleft(5)
print(p)
