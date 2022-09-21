from minimum_window_substringII import Solution
assert Solution().minWindow("ADOBECODEBANC","ABC") == "BANC"
assert Solution().minWindow("defaultdict","adc") == "aultdic"
assert Solution().minWindow("a","aa") == ""
assert Solution().minWindow("aa","aa") == "aa"
assert Solution().minWindow("acbbaca","aba") == "baca"
assert Solution().minWindow("abcdef", "g") == ""