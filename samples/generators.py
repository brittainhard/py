import types

"""
By putting parens instead of brackets you get a generator object.
"""
a = [x for x in range(10)]
b = (x for x in range(10))

def test_type():
    assert isinstance(a, list)
    assert isinstance(b, types.GeneratorType)


"""
Generators are lazy evaluation. The generator is not evaluated unless directly
iterated on.
"""
def test_iterate():
    for x in a:
        print(x)


"""
Generator Function
"""
def generate():
    for x in range(10):
        yield x

def test_get_generator():
    b = generate()
    for x in b:
        assert isinstance(x, int)

