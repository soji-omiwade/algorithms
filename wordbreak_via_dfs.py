'''
s = "leetcode", 
wordDict = ["leet","code"]
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def clear_if_possible(sloc, word):
            if wordaslist == arr[i:i+len(word)]:
                arr[i:i+len(word)] = [None] * len(word)
    
        def helper():
            for word in wordlist:
                if tuple(word) in unavailable:
                    continue
                unavailable.add(tuple(word))
                temparr = list(arr)
                for i in range(len(arr)):
                    clear_if_possible(i, word)
                    if not any(arr):
                        return True
                    breakable = helper()
                    if breakable:
                        return True
                arr = temparr
                unavailable.remove(word)
            return False
                    
        arr = list(s)
        unavailable = set()
        wordlist = [list(word) for word in wordDict]
        return helper()