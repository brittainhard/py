"""
The deal here is that you just add the flag to the end to make sure you ignore
the case. You can really do this work the regex itself, but whatever. Probably.
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'

matches = re.findall('python', text, flags=re.IGNORECASE)

# This one has a problem in that it won't keep the same case when you replace
# the thing you are trying to change. You can create a new function to handle
# this case.
snakes = re.sub('python', 'snake', text, flags=re.IGNORECASE)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

# This is a fix for the problem, here.
better_snakes = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)

print(matches)
print(snakes)
print(better_snakes)
