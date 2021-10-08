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

g, ooog
og, ooog
oog, ooog
ooog, ooig
oooog, ooig

def matches(pattern, string)
    if not pattern and string:
        return False
        
    if pattern[1] == "*"
        done = False
        buffer = ""
        while len(buffer) <= len(string) or done:           # 1 <= 4
            done = matches(buffer + pattern[2:], string)
            buffer += pattern[0]
        return done
    return (
            string
            and pattern[0] in (string[0], '.') 
            and matches(pattern[1:], string[1:])
...
'''

def matches(pattern: str, string: str) -> bool:
    return (pattern[0] == '.' or pattern[0] == string[0] 
        and matches(pattern[1:], string[1:])