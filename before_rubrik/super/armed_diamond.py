class Two: pass
class Five: pass
class Four: pass
class One(Two, Five): pass
class Three(Four, Five): pass
class Zero(One, Three): pass