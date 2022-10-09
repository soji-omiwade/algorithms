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


aaaab
a*b

aaaa
a*

text=aaa
patt=b*aa


''
a*

examples of no pattern:
''
''

text = 'fish'
text = ''

Input:
 
"abaa"
"a.*a*"
res should be true

t = abaa
p = a.*a
t = baa
p = .*a

'''

def is_match(text, pattern):
  # if pattern is empty; then return true if text is also empty,
  # otherwise (text is not empty), return False
  if not pattern:
    return not text

  # pattern not empty
  # may be a regular char, or a * star
  if len(pattern) == 1 or pattern[1] != '*':
    return text and pattern[0] in (".", text[0]) and is_match(text[1:], pattern[1:])
  else:
    zero = is_match(text, pattern[2:])
    mult = text and pattern[0] in ('.', text[0]) and is_match(text[1:], pattern)
    return zero or mult

text = "abaa"
pattern = "a.*a"
print(is_match(text, pattern))

text = "aa"
pattern = "a"
print(is_match(text, pattern))

text = "aa"
pattern = "aa"
print(is_match(text, pattern))

text = "abc"
pattern = "a.c"
print(is_match(text, pattern))

text = "abc"
pattern = "a.d"
print(is_match(text, pattern))
