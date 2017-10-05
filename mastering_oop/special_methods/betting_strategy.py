import abc


class BettingStrategy:

    def bet(self):
        raise NotImplementedError("No such bet metod")

    def record_win(self):
        pass

    def record_loss(self):
        pass


class Flat(BettingStrategy):

    def bet(self):
        return 1


class MetaBettingStrategy(metaclass=abc.ABCMeta):
    """This is only here because it is a way to enfoce that the bet method is
    defined."""

    @abc.abstractmethod
    def bet(self):
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass
