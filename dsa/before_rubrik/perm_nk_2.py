def perm(string, n, k):
    def valid(ch):
        #O(n)
        for chp in arr:
            if chp is None:
                return True
            if chp == ch:
                return False
        raise Exception("impossible to be here")
        
    def helper():
        '''
            find an empty place in arr
            if you cannot
                create a new string out of arr and add it to res
            for every valid number in n-possibilities, place valid number in there
                #valid means it's not already in arr
                recursively do the same two above
        '''
        try:
            emptypos = arr.index(None)  #0
        except ValueError:
            res.append("".join(arr))
            return
        for ch in string:
            if valid(ch):
                arr[emptypos] = ch
                helper()
                arr[emptypos] = None
               
    res = []
    arr = [None] * k
    helper()
    assert arr == [None] * k
    return res
    
res = perm('abcd', 4, 4)
from pprint import pprint
pprint(res) #should be 24!
print(len(res))

res = perm('abcde', 5, 3)
from pprint import pprint
pprint(res)
print(len(res)) #should be 60!

'''
abcd
abdc
acbd
...
'''
