class D: pass
class C: pass
class B(D, C): pass

try:
    class A(B, C, D): pass
except TypeError as te:
    msg = "Cannot create a consistent method resolution"
    msg += "\norder (MRO) for bases D, C"    
    assert te.args[0] == msg
else:
    raise Exception("Type error should have been thrown: MRO is out of whack")