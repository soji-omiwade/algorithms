class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        reqcount = Counter(t)
        count = Counter()
        i = 0
        im, jm = 0, len(s)
        all = 0
        for j in range(len(s)):
            if s[j] in reqcount:
                count[s[j]] += 1
                if count[s[j]] == reqcount[s[j]]:
                    all += 1
                while all == len(reqcount):
                    if j - i < jm - im:
                        im, jm = i, j
                    if s[i] in reqcount:
                        count[s[i]] -= 1
                        if count[s[i]] < reqcount[s[i]]:
                            all -= 1
                    i += 1
        if jm == len(s):
            return ''
        return s[im:jm+1]
        
minwindow = Solution().minWindow
assert minwindow('ADOBECODEBANC', 'ABC') == 'BANC'
assert minwindow('ADOBECODEBANC', 'ABCQ') == ''
assert minwindow('AA', 'AA') == 'AA'
assert minwindow('', '') == ''