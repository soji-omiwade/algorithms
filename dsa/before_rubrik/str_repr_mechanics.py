class Qoo:
    # def __repr__(self):
        # return "repr-start-" + super().__repr__() + "-repr-end"
        
    # def __str__(self):
        # return "str-start-" + super().__str__() + "-str-end"
    nothing_class_var = 42
    def foo(self, a):
        return a
    @classmethod
    def coo(cls, b):
        return b + cls.nothing_class_var
    pass
q = Qoo()
assert Qoo.coo(10) == 52
assert q.foo(422) == 422
assert str(q) == repr(q)
