class Solution:
    def itoa(self, k: int)->str:
        """
        934
        push 4. then 3. then 9. (stack) O(digits in k)
        then pop items in stack into a character array O(digits in k)
        """
        if k==0:
            return "0"
        is_neg = ""
        if k < 0:
            is_neg="-"
            k=abs(k)
        a=[]
        while k != 0:
            """now we fill a with 4 3 9"""
            """how to get the ascii of a number"""
            val = chr((k%10)+ord("0"))
            a.append(val)
            k=k//10
        b=[is_neg]
        while a:
            b.append(a.pop())
        return "".join(b)
            
assert Solution().itoa(891234) == "891234"
assert Solution().itoa(-42) == "-42"
assert Solution().itoa(0) == "0"
