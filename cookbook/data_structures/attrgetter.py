import operator

from functools import partial

class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)


users = [User(23), User(3), User(99)]

users_reg = partial(sorted, users, key=lambda u: u.user_id)
users_attrgetter = partial(sorted, users, key=operator.attrgetter("user_id"))
