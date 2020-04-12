from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def clean(email):
            res = list(email)
            for i in range(len(res)):
                if res[i] == "@":
                    break
                if res[i] == ".":
                    res[i] = None
                if res[i] == "+":
                    res[i] = None
                    if res[i+1] != "@":
                        res[i+1] = "+"
            res2 = []
            for ch in res:
                if ch:
                    res2.append(ch)
            return "".join(res2)
                    
        mails = set([])
        for email in emails:
            clean_email = clean(email)
            mails.add(clean_email)
        return len(mails)

emails = ["apple@foo.com", "app.l.e+rice@foo.com", "a.p.ple@foo.com"]
assert Solution().numUniqueEmails(emails) == 1
emails = ["apple@fo.o.com", "app.l.e+rice@fo.o.com", "a.p.ple@foo.com"]
assert Solution().numUniqueEmails(emails) == 2
emails = ["apple@foo.com", "ap.l.e+rice@foo.com", "a.p.ple@foo.co"]
assert Solution().numUniqueEmails(emails) == 3
