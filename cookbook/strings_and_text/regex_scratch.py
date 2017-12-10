import re

pat = re.compile(r"^(.)..\1*$")

a = pat.search("abba")
print(a)
