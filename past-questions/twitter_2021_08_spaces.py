'''
spacelookup: spacename --> userlookup
userlookup: user --> duration
'''
from collections import defaultdict
from typing import List, Tuple

def spacetime(requests: List[List[str]]) -> List[Tuple[str, int]]:
    spacelookup = defaultdict(lambda : defaultdict(int))
    totallookup = defaultdict(int)
    for action, spacename, userid, timestamp in requests:
        if action in ("create", "join"):
            spacelookup[spacename][userid] = - int(timestamp)
        else: # leave
            spacelookup[spacename][userid] += int(timestamp)
            totallookup[spacename] += spacelookup[spacename][userid]
    return list(totallookup.items())
    
requests = [
    ["create", "abc", "1", "100"], 
    ["join", "abc", "2", "105"], 
    ["create", "xyz", "1", "50"], 
    ["leave", "abc", "1", "110"], 
    ["leave", "abc", "2", "120"], 
    ["leave", "xyz", "1", "70"],    
]
print(spacetime(requests))
'''out should be
[
    [abc, 25]
    [xyz, 20]
]
'''



'''
now you are given logs, but we want to know the top k by number of people
inside such

solution: use heap..why top k
but need to account for 
'''