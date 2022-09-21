'''
for each item in the string
    if item is open
        lastitem = item
        count[item-type] += 1
    else
        if lastitem is not same type as item and last-item is an open
            return false
    
if count[item-type] <----any item-type is greater than 1
    return False
    
return True
    
t: O(n)
s: O(1)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        def itemtype(item):
            if item in "()":
                return "circle"
            if item in "{}":
                return "curly"
            if item in "[]":
                return "square"
            raise ValueError("invalid item")
            
        receiveditems = []
        lastitem = None
        for item in s:
            if item in "([{":
                receiveditems.append(item)
            else:
                if not receiveditems or receiveditems[-1] not in "({[" or itemtype(receiveditems[-1]) != itemtype(item):
                    return False
                receiveditems.pop()
        return not receiveditems
        