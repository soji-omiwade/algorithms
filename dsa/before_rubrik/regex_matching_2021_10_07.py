'''
problem: given a pattern having . (wildcard) and * (zero or more of preceeding char), return true if pattern matches string
examples:
    fish        fisk     -> false
    fi.h        fish     -> true
    do*g        dog      -> true
    f.*y        friday   -> true
    da*bq*q     dbqq     -> true
assumptions/constraints:
approaches:
tradeoffs discussion:

o*g  ooog
    g    --> False
    og   --> F
    oog  --> F
    ooog --> T
o*g
           o + o*g
g, ooog
og, ooog
oog, ooog
ooog, ooig
oooog, ooig

o*g ooog
o*g oog

o*g..., oog...  fail
o*g..., og...   fail
o*g..., g...
def matches(pattern, string)   o*g..., oog...
    if not pattern:
        return not string
        
    if len(pattern) > 1 and pattern[1] == "*"
        return (matches(pattern[2:], string)
                    or (string[0] == pattern[0] and matches(pattern, string[1:]))
               )
    return (
            bool(string)
            and pattern[0] in (string[0], '.') 
            and matches(pattern[1:], string[1:])
...
'''

def matches(pattern: str, string: str) -> bool:
    if not pattern:
        return not string
        
    if len(pattern) > 1 and pattern[1] == "*":
        return (matches(pattern[2:], string)
                    or (string[0] == pattern[0] and matches(pattern, string[1:]))
               )
    return (
            bool(string)
            and pattern[0] in (string[0], '.') 
            and matches(pattern[1:], string[1:])
           )
           
'''
    fish        fisk     -> false
    fi.h        fish     -> true
    do*g        dog      -> true
    f.*y        friday   -> true
    da*bq*q     dbqq     -> true

'''           
pattern, string = "fish", "fisk"           
print(matches(pattern, string)) # F

pattern, string = "fi.h", "fish"           
print(matches(pattern, string)) # T

pattern, string = "do*g", "dog"           
print(matches(pattern, string)) # T

pattern, string = "o*g...", "oog.K."           
print(matches(pattern, string)) # T

pattern, string = "o*g.K.", "oog..."           
print(matches(pattern, string)) # F
