import re

text = "yeah, but no, but yeah, but no, but yeah"
dates = "Today is 11/27/2012. Pycon starts 3/13/2013."

# Simple text replacing.
a = text.replace("yeah", "yep")

# Example using re.sub.
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
replace = r'\3-\1-\2'
sub = re.sub(pattern, replace, dates)
sub2 = pattern.sub(replace, dates)

# This can be used to find out how many substitutions were made.
nums, n = pattern.subn(replace, dates)

# Use of callback statements
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


callback = pattern.sub(change_date, dates)
