def go(sentence):
    import re
    """reverse a string of words
    """
    u = []
    p = re.compile(r'\w+')
    spaces_tokens = p.split(sentence)
    
    #could be done with the findall
    def consume():
        for foo, s in zip(spaces_tokens,p.findall(sentence)):
            print(f"duo: '{foo}'--'{s}'")
            u.append(foo+s[-1::-1])

    #this uses the iterator p.finditer
    def consume_iter():
        for foo, match in zip(spaces_tokens,p.finditer(sentence)):
            print(f"duo: '{foo}'--'{match.group()}'")
            u.append(foo+match.group()[-1::-1])
    
    consume()
    u.append(spaces_tokens[-1])
    return ''.join(u)
    
def go_no_regex(sentence):
    #reverse a string of words without using the regular expressions.
    #because strings are immutable in python, we use a list to simulate 
    #a mutable string
    foo = list(sentence)    
    in_string = False
    def reverse(foo, a, b):
        for i in range(a,(a+b)//2):
            foo[i],foo[b-(i-a)-1] = foo[b-(i-a)-1], foo[i]
    
    for i in range(1+len(foo)):
        if i<len(foo) and foo[i]!=" " and not in_string:
            in_string = True
            start = i
        elif in_string and (i==len(foo) or foo[i]==" "):
            reverse(foo, start,i)
            in_string = False
        else:
            pass
    return ''.join(foo)