'''
problem: word break
example:
    word, comps = "abcde", [bc, de] -> ans = false
    word, comps = "abcde", [bcde] -> ans = false
    word, comps = "abcde", [a, bc, de] -> ans = true
approach-memo
    a bcde; ab cde; abc de; abcd e; abcde ""
    b cde; bc de
    c de; cd e
    d e
    e ""
    return helper(word)
    function helper(word)
        if not word
            return True
            
        ans = False
        for i in range(0, len(word))
            ans = ans or (word[:i+1] in comps  and  helper(word[i+1:]))
        return ans
    time: 
'''
#memoization
def wordbreak(word, dict_):
    return helper(word, set(dict_))

#tabulation...
def wordbreak(word, dict_):
    dict_ = set(dict_)
    f = [False for _ in range(len(word) + 1)]
    f[0] = True
    for k in range(1, len(word)+1):
        for i in range(k-1, -1, -1):
            f[k] = f[k] or (f[i] and word[i:k] in dict_)
    return f[-1]


def helper(word, dict_, memo=None):
    if memo is None:
        memo = {}
    if word in memo:
        print(f"memo[{word}]: {memo[word]}")
        return memo[word]
    if not word:
        return True
        
    ans = False
    for i in range(len(word)):
        subres = helper(word[i+1:], dict_, memo)
        ans = ans or (word[:i+1] in dict_  and  subres)
    memo[word] = ans
    # print(word, memo)
    return ans

word, comps = "abcde", ["bc", 'de'] #-> ans = false
print(wordbreak(word, comps))
word, comps = "abcde", ['bcde'] #-> ans = false
print(wordbreak(word, comps))
word, comps = "abcde", ['a', 'de', 'bc',] #-> ans = true
print(wordbreak(word, comps))
word, comps = "abcde", ['bcde', 'a'] #-> ans = true
print(wordbreak(word, comps))
