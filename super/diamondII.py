class Seven:
    pass
class Six(Seven):
    pass
class Five(Seven):
    pass
class Four(Six):
    pass
class Three(Five,Six):
    pass
class Two(Five):
    pass
class One(Two,Three,Four):
    pass
    
a = [One,Two,Three,Four,Five,Six,Seven]
for _classname in a:
    print(_classname.mro())