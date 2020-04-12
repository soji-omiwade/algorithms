class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def transform(s: str) -> str:
            arr = []
            backspace_next = 0
            for i in range(len(s)-1,-1,-1):
                if s[i] == "#":
                    backspace_next += 1
                    continue
                if backspace_next > 0:
                    backspace_next -= 1
                    continue
                arr.append(s[i])
            return "".join(arr[-1::-1])
        if transform(S) == transform(T):
            return True
        return False

assert Solution().backspaceCompare("ab#c","ad#c")
assert not Solution().backspaceCompare("ab#c", "ad#d")
assert Solution().backspaceCompare("###d", "#d")