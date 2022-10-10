'''
p = a a .  b *   q 
t = a a c [q/b]

p -- b *
t -- c 

0
b b
b b b

--> true

p 0 bs --rest of patter
p 1 b + rest of pattern

func(t, p)
  if p[1] != * and they are not equal
    return false
  if t[0] == p[0] or p[0] == .    
     return func(t[1:], p[1:])
  if p[]
time comp = |p|  |t|
space = |t|

is_match(text, pattern, 0, 0) # initial call

is_match(text, pattern, text_index, pattern_index)



aaaa
a*
'''

'''
t(n) = 2 * t(n-1)
'''
def is_match(text, pattern):
    def is_match(text, pattern, tloc, ploc):
        # if pattern is empty; then return true if text is also empty,
        # otherwise (text is not empty), return False
        if ploc == len(pattern):
            #desire True if no more text left. otherwise false
            return tloc == len(text)

        # pattern not empty
        # may be a regular char, or a * star
        if ploc == len(pattern) - 1  or pattern[1 + ploc] != '*':
          return tloc < len(text) and pattern[ploc] in (".", text[tloc]) and \
                  is_match(text, pattern, tloc + 1, ploc + 1)
        else:
          zero = is_match(text, pattern, tloc, 2 + ploc)
          mult = tloc < len(text) and pattern[ploc] in ('.', text[tloc]) and \
                  is_match(text, pattern, 1 + tloc, ploc)
          return zero or mult
    return is_match(text, pattern, 0, 0)
  
text = "abaa"
pattern = "a.*a"
print(is_match(text, pattern))

text = "aa"
pattern = "aa"
print(is_match(text, pattern))

text = "aa"
pattern = "a"
print(is_match(text, pattern))

text = "abc"
pattern = "a.c"
print(is_match(text, pattern))

text = "abc"
pattern = "a.d"
print(is_match(text, pattern))

