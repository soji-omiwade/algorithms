class Solution:
    def isValid(self, s: str) -> bool:
        def opposite(ch):
            if ch == "]": return "["
            if ch=="}": return "{"
            if ch==")": return "("
        a=[]
        for ch in s:
            if ch in "[({":
                a.append(ch)
            elif len(a) == 0 or a.pop()!=opposite(ch):
                return False
        if a:
            return False
        return True
        
assert not Solution().isValid("[)")
assert not Solution().isValid("][")
assert Solution().isValid("()")
assert Solution().isValid("({[]})")
assert Solution().isValid("")
assert not Solution().isValid("((")

