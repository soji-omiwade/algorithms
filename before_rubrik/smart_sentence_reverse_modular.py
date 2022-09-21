"""
Given a string with words and arbirary spaces between the words, reverse all words within the string
"""

def go(s: str):
    s = list(s)
    in_word = False
    start = end = None
    for i in range(1+len(s)):
        if i==len(s) or (s[i] == " " and in_word):
            in_word = False
            end = i
        elif s[i] != " " and not in_word:
            in_word = True
            start = i
        
        if start is not None and end is not None:
            for i in range(start, (start+end)//2):
                s[i],s[end-(i-start)-1] = s[end-(i-start)-1],s[i]
            start = end = None
            
    return "".join(s)
    
import unittest
class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(go("I love   to eat"), "I evol   ot tae")
        self.assertEqual(go("   "), "   ")
        
unittest.main(verbosity=2)

# print(go("I love   to eat"))