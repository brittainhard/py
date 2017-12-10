"""
I think the lesson here is that you should NEVER use re.match. The only reason
you would use it is because you want to write a regex pattern without including
the '^' in the front of the pattern. Doesn't really make sense otherwise.

Findall works great, and you should use it when you are looking for a pattern in
a large amount of text. Thankfully, findall doesnt seem to care whether there
are newlines in the text.
"""

import re

text1 = "11/27/2012"
text2 = "Nov 27, 2012"
text3 = "Today is 11/27/2012. Pycon starts 3/13/2013."
text4 = "Today is 11/27/2012. \nPycon starts 3/13/2013."

pattern = re.compile(r"\d+/\d+/\d+")
pattern2 = re.compile(r"(\d+)/(\d+)/(\d+)")

"""Works because the stuff you are looking for is at the beginning of the
string."""
a = pattern.search(text1)
"""Fails, obviously. Returns nothing"""
b = pattern.search(text2)
"""Instead of returning True or False, it returns all of the items matched in a
particular string."""
c = pattern.findall(text3)
"""Fails again because the text to be looked for is not at the beginning."""
d = pattern.match(text3)

"""Interesting thing happening here with `e`. It is automatically looking
through the groups looking for matches, and it returns all the groups."""
e = pattern2.search(text3)
# This returns all the items as a list of tuples.
f = pattern2.findall(text3)
"""This was to test if it can handle newlines. It can."""
g = pattern2.findall(text4)

# Returns an iterator. Just like a generator.
h = pattern2.finditer(text3)

month, day, year = e.groups()

