'Demonstrate effective use of super()'

import collections
import logging

logging.basicConfig(level='INFO')

class LoggingDict(dict):
    # Simple example of extending a builtin class
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super().__setitem__(key, value)

class LoggingOD(LoggingDict, collections.OrderedDict):
    # Build new functionality by reordering the MRO
    pass

ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
print(ld)
ld['red'] = 10

ld = LoggingOD([('red', 1), ('green', 2), ('blue', 3)])
print(ld)
ld['red'] = 10
print('-' * 20)

#show call order
#------show the order that the methods are called
def show_call_order(cls, methname):
    'utility to show the call chain'
    classes = [cls for cls in cls.__mro__ if methname in cls.__dict__]
    print('  ==>  '.join('%s.%s' % (cls.__name__, methname ) for cls in classes))
    
show_call_order(LoggingOD, '__setitem__')
show_call_order(LoggingOD, "__iter__")
print("-" * 20)

#---------Validate and document any call order requirements------
position = LoggingOD.mro().index
assert position(LoggingDict) < position(collections.OrderedDict) < position(dict)
it = iter(LoggingOD)
it = iter(LoggingDict)


#--------Getting the argument's signature to match
