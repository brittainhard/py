class Foo:
    """
    Python is a consenting adult's language. No such thing as private and public
    methods.

    If this leads me away from doing this very natural thing, then its
    definitely to be stopped. I know you didn't need to need. Needing. Needling
    """

    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass
