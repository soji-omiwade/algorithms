class Root:
    def draw(self):
        print(__class__, "the delegation chain stops here")
        assert not hasattr(super(), "draw")

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, error):
        print(__class__, error, "drawing at position:", self.x, self.y)

class MoveableAdapterPrime(Root):
    def draw(self, **kwargs):
        print(__class__, "drawing nothing parent. just testing python mro")
        super().draw(**kwargs)
    
class MoveableAdapter(MoveableAdapterPrime):
    def __init__(self, x, y, **kwargs):
        self.movable = Moveable(x, y)
        super().__init__(**kwargs)
    def draw(self, error, **kwargs):
        print(__class__, "drawing nothing. just testing python mro")
        self.movable.draw(error)
        super().draw(**kwargs)

class Shape(Root):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super().__init__(**kwargs)
    def draw(self, **kwargs):
        print(__class__, "Drawing. Setting shape to:", self.shapename)
        super().draw(**kwargs)
        
class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super(ColoredShape, self).__init__(**kwargs)
    def draw(self, **kwargs):
        print(__class__, "drawing. setting color to:", self.color)
        super().draw(**kwargs)
        
class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass

cs = ColoredShape(color="red", shapename="triangle")
cs.draw()
    
mcs = MovableColoredShape(color="red", shapename="circle", x=2, y=3)
assert (mcs.movable.x, mcs.movable.y) == (2,3)
mcs.draw(error=42)
