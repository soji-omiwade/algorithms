class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(lo, maxhi):
            if lo == maxhi:#
                return True
            for hi in range(lo + 1, maxhi + 1): # [1, 2, 3, ..., 2) = [1]
                if (hi,maxhi) not in memo:
                    memo[(hi,maxhi)] = helper(hi, maxhi)
                if s[lo:hi] in words and memo[(hi,maxhi)]:
                    return True
            return False
        memo = {}
        words = set(wordDict)
        return helper(0, len(s))