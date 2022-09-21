class Root2:
    def sought(self):
        return "root2"

class Root(Root2):
    def draw(self):
        print("the delegation chain about to stop")
        super().draw()
    
class Other2:
    def sought(self):
        return "other2"
        
class Other(Other2):
    def draw(self):
        print("other drawing. other doing a draw")
        super().draw()
    
class Shape(Other, Root):
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super().__init__(**kwargs)
    def draw(self):
        print("Drawing. Setting shape to: ", self.shapename)
        super().draw()
        
class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super(ColoredShape, self).__init__(**kwargs)
    def draw(self):
        print("drawing. setting color to:", self.color)
        super().draw()
        
cs = ColoredShape(color="red", shapename="circle")
assert cs.sought() == "other2"