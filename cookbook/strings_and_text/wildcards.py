import re
from fnmatch import fnmatch, fnmatchcase

a = fnmatch("foo.txt", "*.txt")

# This will return false on mac but true on windows
# in which case you should use fnmatchcase.
b = fnmatch("foo.txt", "*.TXT")
c = fnmatchcase("foo.txt", "*.TXT")

print(a)
print(b)
print(c)

# Regex and Wildcard examples. Tried to use re.match here and it failed
# miserably. Not totally sure how to match something...
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

d = [name for name in names if fnmatch(name, 'Dat*.csv')]
e = [name for name in names if re.search('.csv', name)]

print(d)
print(e)

"""
To sum up: never use re.match. It only matches from the beginning. re.search is
what you want. Why would you want re.match at all? You can do everything in
re.search that you can do in re.match.
"""
