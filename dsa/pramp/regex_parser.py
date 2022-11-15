'''
pattern
aba
aba

a.c
abc

abcc
ab*cc

abcc
ab*cc

if no *
  when curridx of text and pattern match, move on
  if not return false
if a * is there

if we have p=x* or empty, and t='', we can return true
if p = '', and t is not empty, we are not good
if p = '', t = '', we are good

p, t
e, ne -> false
e, e, -> true
ne, e -> depends on what p is
ne, ne -> depends on both!
'''
def charmatch(tch, pch):
  return pch in (tch, '.')
def is_match(text, pattern):
  if not pattern:
    return not text
  #pattern is not empty:
  if len(pattern) > 1 and pattern[1] == '*':
    #raise Exception("not implemented")
    return is_match(text, pattern[2:]) or \
            (charmatch(text[0], pattern[0]) and is_match(text[1:], pattern))
  else: #no * after the first char of pattern
    return charmatch(text[0], pattern[0]) and is_match(text[1:], pattern[1:])
  
text = "aa"
pattern = "a"
print (is_match(text, pattern))
text = "aa"
pattern = "aa"
print (is_match(text, pattern))
text = "abc"
pattern = "a.c"
print (is_match(text, pattern))
text = "abbb"
pattern = "ab*"
print (is_match(text, pattern))

