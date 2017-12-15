"""
No citrix, no remembering passwords, no finding things to do, no stress, no...

The Republican party is the enemy. Childish thought.
"""

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}',
}


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
print(format(d))
print(format(d, "mdy"))
print(format(d, "dmy"))

# Use this thing if you want to access a dictionary by a specific key. It
# doesn't look like he put it anywhere else in the book. Important to catch that
# one. I didn't think there was so much to the format function.
print("The date is {:ymd}".format(d))
