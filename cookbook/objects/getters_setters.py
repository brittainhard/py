"""
'Getters, Setters' AKA 'managed atributes'. Probably a better example of getters and setters that in
the lecture, although that lecture was only 50 minutes long.

A better name, 'Customizing access to an attribute'.

Make sure you do scratch stuff for these things. No sense in not playing around
with scratch programs.

Just keep your head down. Down.

I break mirrors with my face in the united states.
"""

class Person:
    """
    In this example, you are validating the type of the value.

    In reality, you should only change an attribute to a property if you need to
    do some extra processing on the input.

    This can be useful for calculating things like area for a circle.
    """

    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter Function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        print("Deleting")
        raise AttributeError("Can't delete an attribute")


a = Person("Kelly")
