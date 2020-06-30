class Animal:
    def foo(self): 
        print(__class__)
        # super().foo()
        assert not hasattr(super(), "foo")
class WingedAnimalParent(Animal):
    def foo(self): 
        print(__class__)
        super().foo()
class MammalParent(Animal):
    def foo(self): 
        print(__class__)
        super().foo()
class WingedAnimal(WingedAnimalParent):
    def foo(self): 
        print(__class__)
        super().foo()
class Mammal(MammalParent):
    def foo(self): 
        print(__class__)
        super().foo()
class Bat(WingedAnimal, Mammal):
    def foo(self): 
        print(__class__)
        super().foo()

b = Bat()
b.foo()