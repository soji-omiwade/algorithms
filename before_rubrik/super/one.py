import logging


class LoggingDict(dict):
    # def __setitem__(self, key, value):
        # print('Setting to %r %r' % (key, value))        
        # super().__setitem__(key, value)

    def __setitem__(self, key, value):
        try: 
            self_key = self[key]
        except:
            self_key = None
        print('Setting to %r value from %r %r' % (key, self_key, value))
        super().__setitem__(key, value)
        assert super() != dict
        assert super() is not dict
        assert type(super()) is not type(dict)
# a = LoggingDict()
# a["me"] = "you"

from collections import OrderedDict

class LoggingOD(OrderedDict, LoggingDict):
    pass
    

class Foo:
    def true_diam(self):
        return 43 - self.diameter

class Round(Foo):
    def true_diam(self):
        return 42 - self.diameter

class Ball(Round):
    def true_diam(self):
        return 41 - self.diameter
    def __init__(self, diameter=42):
        self.diameter = diameter

    def add_some_air(self):
        self.diameter += 1
        
    def add_twice_some_air(self):
        for i in range(2):
            # self.add_some_air()
            Ball.add_some_air(self)

    def check_super(self):
        assert self.true_diam() == -1
        assert self.true_diam() ==  Ball.true_diam(self)
        assert super().true_diam() == 0
        assert super(Ball, self).true_diam() == 0
        assert super(Round, self).true_diam() == 1
        
        ball = Ball(); ball.add_twice_some_air();
        assert ball.true_diam() == -3
        assert ball.true_diam() ==  Ball.true_diam(ball)
        assert super().true_diam() == 0
        assert super(Ball, ball).true_diam() == -2
        assert super(Round, ball).true_diam() == -1
        
        a = super() 
        b = super()
        assert a is not b
        
b = Ball()
# b.add_some_air()
# b.add_twice_some_air()
# assert b.diameter == 45
b.check_super()