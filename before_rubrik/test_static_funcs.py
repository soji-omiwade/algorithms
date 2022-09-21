class TestStaticFuncs:
    def foo(self, a, b):
        return self.coo(a, b)
        
    @staticmethod
    def roo(a, b):
        return "r " + str(TestStaticFuncs.coo(a, b))
        
    @staticmethod
    def coo(a, b):
        return (a, b) + (a, b)
        
assert TestStaticFuncs().foo(1,2) == (1,2,1,2)
assert TestStaticFuncs.coo(42,48) == (42, 48, 42, 48)
assert TestStaticFuncs.roo(42, 48) == "r (42, 48, 42, 48)"