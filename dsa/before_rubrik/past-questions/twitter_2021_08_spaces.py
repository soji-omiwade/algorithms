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
but need to account for  changes to heap priorities! let's do it!!

heapentry: [usercount, spacename]
heapentrylookup: spacename --> heapentry

'''
import heapq
def setup():
    heapentrylookup = defaultdict(lambda: [0, None])
    spacesheap = []
    return heapentrylookup, spacesheap
    
'''
    ["create", "abc", "1", "100"], 


requests = [
    ["create", "abc", "1", "100"], 
    ["join", "abc", "2", "105"], 
    ["create", "xyz", "1", "50"],
    ["leave", "abc", "1", "110"], 
    ["leave", "xyz", "1", "70"],        
    ["join", "abc", "3", "110"], 
    ["join", "abc", "4", "120"], 
    ["join", "xyz", "1", "70"],    
    ["join", "xyz", "42", "70"],    
    ["create", "low", "1", "70"],    
]    
'''
def action_happened(action, spacename, userid, timestamp, spacesheap, heapentrylookup):    
    #request should be appended to requests esp. for timestamp
    
    heapentry = heapentrylookup[spacename]
    heapentry[-1] = "REMOVED"   
    newheapentry = [heapentry[0], spacename]
    heapentrylookup[spacename] = newheapentry
    
    if action == "leave":    
        newheapentry[0] += 1
    else: #create or join
        newheapentry[0] -= 1
    heapq.heappush(spacesheap, newheapentry)


def topk(spacesheap, k):
    '''
    remove k; then put them back before returning 
    OR
    copy the list; remove k; and return: O(n) ---> no no
    '''
    have = 0
    tempstore = []
    res = []
    while have < k:
        heapentry = heapq.heappop(spacesheap)
        if heapentry[-1] != "REMOVED":
            tempstore.append(heapentry)
            res.append((heapentry[-1], -heapentry[0]))
            have += 1
    for heapentry in tempstore:
        heapq.heappush(spacesheap, heapentry)
    return res

requests = [
    ["create", "abc", "1", "100"], 
    ["join", "abc", "2", "105"], 
    ["create", "xyz", "1", "50"],
    ["leave", "abc", "1", "110"], 
    ["leave", "xyz", "1", "70"],        
    ["join", "abc", "3", "110"], 
    ["join", "abc", "4", "120"], 
    ["join", "xyz", "1", "70"],    
    ["join", "xyz", "42", "70"],    
    ["create", "low", "1", "70"],    
]    

heapentrylookup, spacesheap= setup()
for action in requests:
    action_happened(*action, spacesheap, heapentrylookup)
print(spacesheap)
print(heapentrylookup)
print(topk(spacesheap, 1)) #output: [abc, 3]
print(topk(spacesheap, 2)) #output: [(abc, 3), (xyz, 2)]
print(topk(spacesheap, 3)) #output: [(abc, 3), (xyz, 2), (low, 1)]