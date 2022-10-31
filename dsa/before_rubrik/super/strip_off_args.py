class Shape:
    def __init__(self, shapename, **kwargs):
        self.shapename = shapename
        super().__init__(**kwargs)
        
class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super(ColoredShape, self).__init__(**kwargs)
        
cs = ColoredShape(shapename="circle", color="red")
assert cs.color == "red"
assert cs.shapename == "circle"