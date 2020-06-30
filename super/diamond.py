class Animal:
    def foo(self):
        return "animal"
class WingedAnimal(Animal):
    def foo(self):
        return "wingedanimal"
class Mammal(Animal):
    def foo(self):
        return "mammal"
class Bat(Mammal, WingedAnimal):
    def foo(self): 
        return super().foo()
bat = Bat()
assert bat.foo() == "mammal"



class Animal:
    def foo(self):
        return "animal"
class WingedAnimal(Animal):
    def foo(self, *args):
        return "wingedanimal"
class Mammal(Animal):
    def foo(self):
        return "mammal"
class Bat(WingedAnimal, Mammal):
    def foo(self): 
        return super().foo("sheep")
bat = Bat()
assert bat.foo() == "wingedanimal"



class Bat(WingedAnimal, Mammal):
    pass
bat = Bat()
assert bat.foo() == "wingedanimal"


class WingedAnimal(Animal):
    def ffoo(self):
        return "wingedanimal"
class Mammal(Animal):
    def foo(self):
        return "mammal"
class Bat(WingedAnimal, Mammal):
    pass
bat = Bat()
assert bat.foo() == "mammal"


class WingedAnimal(Animal):
    def ffoo(self):
        return "wingedanimal"
class Mammal(Animal):
    def ffoo(self):
        return "mammal"
class Bat(WingedAnimal, Mammal):
    pass
bat = Bat()
assert bat.foo() == "animal"
