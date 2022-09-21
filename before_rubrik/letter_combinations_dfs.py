'''
a 
    a or b

b
    a
        a
        
res = helper([]) # the answer
count = Counter(tiles)

function helper(path)
    res = 0
    for letter in count:
        if count[letter] > 0:
            count[letter] -= 1
            res += 1 + helper(path + [letter])
            count[letter] += 1
    return res
'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper(path):
            res = 0
            for letter in count:
                if count[letter] > 0:
                    count[letter] -= 1
                    res += 1 + helper(path + [letter])
                    print("".join(path + [letter]))
                    count[letter] += 1
            return res

        count = Counter(tiles)
        return helper([]) # the answer

