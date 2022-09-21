class B:
    def __init__(self):
        print(__class__, "..initializing")
class C:
    def __init__(self):
        print(__class__, "..initializing")
class A(B,C):
    def __init__(self):
        print(__class__, "..initializing")
                
a = A()

"""
lesson for today.
init doesn't get called. but something else does.
nope. init always gets called!
"""