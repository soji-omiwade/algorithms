class D: pass
class C(D): pass
class BP: pass
class B(D, BP): pass
class A(B, C): pass

assert A.__mro__ == (A, B, C, D, BP, object)


#C possibly may not come immediately  after A, if we remove the C->D constraint


class II_D: pass
class II_C: pass
class II_BP: pass
class II_B(II_D, II_BP): pass
class II_A(II_B, II_C): pass

assert II_A.__mro__ == (II_A, II_B, II_D, II_BP, II_C, object)
