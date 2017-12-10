import re

text = "yeah, but no, but yeah, but no, but yeah"
dates = "Today is 11/27/2012. Pycon starts 3/13/2013."

# Simple text replacing.
a = text.replace("yeah", "yep")

# Example using re.sub.
# pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
# replace = re.compile(r'\3-\1-\2')
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
replace = r'\3-\1-\2'
sub = re.sub(pattern, replace, dates)
sub2 = pattern.sub(replace, dates)

