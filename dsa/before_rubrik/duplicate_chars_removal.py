def go(s):
    s = list(s)
    instring = False
    loc = 0
    for i in range(len(s)):
        if ord(s[i]) >= ord("A") and  ord(s[i]) <= ord("z"):
            if not instring:
                s[loc] = s[i]
                loc += 1
            instring = True
        else:
            instring = False
    return " ".join(s[:loc])
import unittest

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(go("AAA    BB C DDDD"), "A B C D")
        self.assertEqual(go("AAA    BB C DDDD   XXX   "), "A B C D X")
        
unittest.main()