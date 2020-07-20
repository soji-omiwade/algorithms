class D: pass
class C(D): pass
class BP: pass
class B(D, BP): pass

try:
    class A(B, C, BP, D): pass
except TypeError as te:
    msg = "Cannot create a consistent method resolution"
    msg += "\norder (MRO) for bases D, BP"    
    assert te.args[0] == msg
else:
    raise Exception("Type error should have been thrown: MRO is out of whack")