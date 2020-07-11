class E: 
    @classmethod
    def foo(cls, *args, **kwargs):
        raise Exception("shouldn't be called")
        
class D:
    cake = "D"
    @classmethod
    def foo(cls, *args, **kwargs):
        assert cls is A
        assert cls.cake == "A"
        assert D.cake == "D"
        assert len(args) == 0
        assert len(kwargs) == 0
        assert not hasattr(super(D, cls), "foo")
        
class C(D):
    cake = "C"
    @classmethod
    def foo(cls, c, *args, **kwargs):
        assert cls is A
        assert cls.cake == "A"
        assert super().cake == "D"
        assert len(args) == 0
        assert c == "cc"
        assert hasattr(super(), "foo")
        super().foo(**kwargs)
        
class B(D):
    cake = "B"
    @classmethod
    def foo(cls, b, *args, **kwargs):
        assert cls is A
        assert cls.cake == "A"
        assert super().cake == "C"
        assert len(args) == 0
        assert b == "bb"
        assert hasattr(super(), "foo")
        super().foo(**kwargs)

class A(B, C):
    cake = "A"
    @classmethod
    def foo(cls, a, *args, **kwargs):
        assert cls is A
        assert cls.cake == "A"
        assert super().cake == "B"
        assert len(args) == 0
        assert a == "aa"
        assert hasattr(super(), "foo")
        super().foo(**kwargs)

obj = A()
A.foo(a="aa", b="bb", c="cc")
assert A.mro() == [A, B, C, D, object]