class Solution:
    def isValid(self,s):
        st=[]
        for ch in s:
            if ch == "(":
                st.append(")")
            elif ch == "[":
                st.append("]")
            elif ch == "{":
                st.append("}")
            elif len(st)==0 or st.pop() != ch:
                return False
        return len(st)==0
assert not Solution().isValid("[)")
assert not Solution().isValid("][")
assert Solution().isValid("()")
assert Solution().isValid("({[]})")
assert Solution().isValid("")
assert not Solution().isValid("((")
                