class Date:
    """
    If you use slots, then multiple inheritance won't work. Slots is only good
    if you are making millions of instances of a particular class.

    Slots is not a tool for encapsulating stuff. That is, you can still change
    attributes and add or remove attributes.

    Slots is just an optimization tool.
    """

    __slots__ = ["year", "month", "day"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
