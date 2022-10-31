class Root:
    def foo(self, res):
        res += [Root, object]
        return res
class D(Root):
    def foo(self, res):
        res += [D]
        return super().foo(res)
class C(D):
    def foo(self, res):
        res += [C]
        return super().foo(res)
class BP(Root):
    def foo(self, res):
        res += [BP]
        return super().foo(res)
class B(BP, D):
    def foo(self, res):
        res += [B]
        return super().foo(res)
class A(B, C):
    def foo(self, res):
        res += [A]
        return super(C, self).foo(res)
class Myclass(A, B):
    def foo(self, res):
        res += [Myclass]
        return super().foo(res)

assert Myclass.__mro__ == (Myclass, A, B, BP, C, D, Root, object)
assert BP.__mro__ == (BP, Root, object)

mclass = Myclass()
assert tuple(mclass.foo([])) == (Myclass, A, D, Root, object)