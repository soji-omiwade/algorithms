class Nonlocal(object):
    """ Helper to implement nonlocal names in Python 2.x """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Nonlocal2:
    pass

def outer():
    nl = Nonlocal2()
    nl.y = 0
    def inner():
        nl.y += 1
        return nl.y
    return inner

f = outer()
g = outer()
print(f(), g(), f(), f()) # -> (1 2 3)
print(g(), g(), g()) # -> (1 2 3)