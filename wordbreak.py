'''
s = "leetcode", 
wordDict = ["leet","code"]
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = list(s)
        for word in sorted(wordDict, reverse=True):
            wordaslist = list(word)
            for i in range(len(s)):
                if wordaslist == arr[i:i+len(word)]:
                    # print(i, word, s[i:i+len(word)])
                    arr[i:i+len(word)] = [None] * len(word)
        for item in arr:
            if item:
                return False
        else:
            return True
        raise Exception('impossible to be here!')