class Root: pass
class D(Root): pass
class C(D): pass
class BP(Root): pass
class B(BP, D): pass
class A(B, C): pass
class Myclass(A, B): pass
assert Myclass.__mro__ == (Myclass, A, B, BP, C, D, Root, object)