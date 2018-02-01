import pytest


def potato(func):
    def closure(arg):
        return func(arg * 2)
    return closure


@potato
def hey(num):
    return num + 1


def test_get_closure():
    a = potato(4)
    assert a.__closure__
