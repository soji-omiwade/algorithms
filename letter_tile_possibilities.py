
'''
have fun!

A A B
0 1 2

func main
    res = this is an empty  set so AAB and AAB are the same thing
    filled = []
    helper(0)
    return len(res)

func helper(k) 
    if k == len(tiles)
        res.append(tuple(filled))
        return
    for i in range(k, len(tiles))
        filled.append(tiles[i], i + 1)
        helper(k + 1)
        filled.pop()
'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper():
            nonlocal usedcount
            if usedcount == width:
                res.add(tuple(filled))
                return
            # A B A
            for i in range(len(tiles)):
                if not used[i]:
                    filled.append(tiles[i])
                    used[i] = True
                    usedcount += 1
                    helper()
                    filled.pop()
                    used[i] = False
                    usedcount -= 1

        usedcount = 0
        used = [False] * len(tiles)
        res = set()
        filled = []                    
        for width in range(1, 1 + len(tiles)):                    
            helper()
        return len(res)

