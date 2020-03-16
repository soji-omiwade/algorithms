class Solution:
    """find it"""
    
    def countAndSay(self: Solution, n: int = 42) -> str:
        for _ in range(n):
            rem = 
        pattern = "(" + string[k:] + ")+";
        replacement = r"\1"
        res = re.sub(pattern, replacement, string)
        count = len(string) - len(res) + 1
        res.append(str(count))
        return res
        
        
assert Solution().countAndSay(1) == "1"
assert Solution().countAndSay(2) == "11"
assert Solution().countAndSay(3) == "21"
assert Solution().countAndSay(4) == "1211"
assert Solution().countAndSay(5) == "111221"
assert Solution().countAndSay(6) == "312211"
