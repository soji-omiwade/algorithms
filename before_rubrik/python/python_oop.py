class Animal:
    def __init__(self):
        self.has_legs = True
        print("created an animal")


class WingedAnimal(Animal):
    def __init__(self):
        self.has_wings = True
        print("created a winged animal")
        
wa = WingedAnimal()
try:
    wa.has_legs
except AttributeError:
    print("no legs until you call the constructor")
else:
    print("should not be here")

print("----------")    
wla = WingedAnimal()
super(WingedAnimal, wla).__init__()
try:
    wla.has_legs
except AttributeError:
    print("should not be here")
else:
    print("legs since super called you call the constructor")

print("----------")
wa2 = WingedAnimal()
super(Animal, wla).__init__()
try:
    wa2.has_legs
except AttributeError:
    print("no legs until you call the constructor")
else:
    print("shouldnt be here")
