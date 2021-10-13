'''
problem: word break
example:
    word, comps = "abcde", [bc, de] -> ans = false
    word, comps = "abcde", [bcde] -> ans = false
    word, comps = "abcde", [a, bc, de] -> ans = true
approach
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
'''
def wordbreak(word, dict_):
    return helper(word, set(dict_))

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
