class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return []
        res="1"
        for _ in range(n-1):
            s = res
            k = 0
            t = []
            while k < len(s):
                kp, k = k, k + 1
                while k < len(s) and s[k] == s[kp]:
                    k += 1
                t.append(str(k-kp) + s[kp])
            res = "".join(t)
        return res
        
assert Solution().countAndSay(1) == "1"
assert Solution().countAndSay(2) == "11"
assert Solution().countAndSay(3) == "21"
assert Solution().countAndSay(4) == "1211"
assert Solution().countAndSay(5) == "111221"
assert Solution().countAndSay(6) == "312211"
