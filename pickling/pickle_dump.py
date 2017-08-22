"""
# Pickling

Good for serializing objects and passing them. This is pretty well comprimised by
the fact that you have to import the necessary modules.

So in the main, any imports used in the object are saved and can be called on.

## Libraries and Enivironments

A library does not have to be in the same environment to be used for pickling.
Naturally, you have to have the library somewhere on your system. Interestingly,
the file itself will record where the import came from, and will automatically
import it for you.

It is important to know that you cannot pickle modules. You can pickle references
to an import to be used later, but you cannot pickle the module itself.

# Project Ideas

Create a program that will allow you to save module objects as pickles and pass
them forward in a file.
"""

import pickle
import datetime
import cython
from pprint import pprint


class Potato:

    def __init__(self, potato):
        """
        You will get a `TypeError: can't pickle module objects` if you try to
        set the imports as attibutes on the object itself, like this:

        self.datetime = datetime
        self.cython = cython
        """
        self.potato = potato

    def print_potato(self):
        """
        Prints the module at the place where it can be imported. Pickling will
        save the location of this module.
        """
        print(datetime)
        print(cython)
        pprint(self.potato)


a = Potato("potato")
pickle.dump(a, open("saved.p", "wb"))
