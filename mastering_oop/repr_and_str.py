class Potato:

    def __init__(self, potato, apple):
        self.potato = potato
        self.apple = apple

    def __repr__(self):
        """This is what shows up when you try to investigate what something is,
        for example, when you are debugging."""
        repr_string = "{__class__.__name__}(potato={potato!s}, apple={apple!s})"
        return repr_string.format(__class__=self.__class__, **self.__dict__)

    def __str__(self):
        """This is what shows up when you print something."""
        return "{potato} {apple}".format(**self.__dict__)


class PotatoSack:

    def __init__(self, potatoes):
        self.potatoes = list(potatoes)

    def __str__(self):
        return ", ".join(map(str, self.potatoes))

    def __repr__(self):
        repr_string = "{__class__.__name__}({_potato_str})"
        return repr_string.format(
            __class__ = self.__class__,
            _potato_str=",".join(map(repr, self.potatoes)),
        )

content = "For a long time I used to go to bed early."
# Pretty sure this calls the split function twice. Not he best.
potatoes = PotatoSack(list(map(Potato, content.split(" "), range(len(content.split(" "))))))
