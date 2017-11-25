from collections import namedtuple

"""
Named tuple can be used as a replacement for a dictionary, since it is much
faster. If you need to make changes to attributes, however, using a class with
__slots__ might be a better idea.
"""

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jonesy@example.com", "2012-10-19")
print(sub)
print(sub.addr)
