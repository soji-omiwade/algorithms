import unittest

def grep(needle, haystack):
    foo = []
    m,n = len(haystack), len(needle)
    for i in range(m-n+1):
        matches = False
        for j in range(n):
            if needle[j] != haystack[i+j]:
                break
        else: matches = True
        if matches:
            foo.append(i)
    return foo
    
def fast_grep(needle, haystack):
    foo = []
    m,n = len(haystack), len(needle)
    val = 0
    mag = 256
    if m < n: return []
    
    if n == 0: return [i for i in range(m+1)]
    val = val2 = 0
    for i in range(n):
        val += ord(needle[i]) * mag ** i
        val2 += ord(haystack[i]) * mag ** i
    if val == val2:
        foo.append(0)
        
    for i in range(m-n):
        val2 -= ord(haystack[i])
        val2 //= mag
        val2 += ord(haystack[i+n]) * mag ** (n-1)
        if val == val2:
            foo.append(i+1)
    return foo
    
class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(grep("aaa", "aaaaa"), [0,1,2])
        self.assertEqual(grep("ab", "aaba"), [1])
        self.assertEqual(grep("", "abcde"), [0,1,2,3,4,5])
        self.assertEqual(grep("abc", "jackabcbeanabc"), [4,11])

    def test_fast_grep(self):
        self.assertEqual(fast_grep("aaa", "aaaaa"), [0,1,2])
        self.assertEqual(fast_grep("ab", "aaba"), [1])
        self.assertEqual(fast_grep("abc", "jackabcbeanabc"), [4,11])
        self.assertEqual(fast_grep("", "abcde"), [0,1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()