from typing import List, Optional
from collections import Counter

'''
string = bbabylkkj
sorted = 
0123456789
abbbjkkly
alist = [0]
blist = [1,2,3]
jlist = [4]
klist = [5,6]
llist = [7]
ylist = [8] 
now given word, say baby.
for each letter in word
    loc = binsearch in lookup[letter]
    if loc is outside of that lookup[letter], then it isn't in T
example

cat -> act
baby -> abby

0123456789
abbbjkkly
act
abby

bsear

   
- sort every single string!
- string to arrays (of indexes). example: 
    string

T: O(L lg L + L + k*(W lg W + W lgL))
S: O(L+ L lg L + W lg W)
'''
from bisect import bisect_left
from collections import defaultdict
def binsearch_find_scrambled(words: List[str], string:str) -> Optional[str]:
    '''
    cat
    tt**********ac
    act
    a****c***a**tt
    a -> [0, 7]
    c -> [5]
    t -> [10, 11]
    ni -> 0--6
    
    baby ->      abby
    baykkjl ->   abjkkly
    '''
    sortedstring = sorted(string)
    letterlookup = defaultdict(list)
    for loc, letter in enumerate(sortedstring):
        letterlookup[letter].append(loc)
    for word in words:
        next_sidx = 0 # forgot to put this in the loop
        sortedword = sorted(word)
        # print(f"word = {word}")
        for letter in sortedword:   # dammit! instead of using sortedword here, I used word. ARGH!!
            loc = bisect_left(letterlookup[letter], next_sidx)
            # print("letter, lookup, nextidx, loc  --> ", letter, letterlookup[letter], next_sidx, loc)
            if loc == len(letterlookup[letter]):
                break
            next_sidx = letterlookup[letter][loc] + 1  #wow i really gotta watch names. next time stick to no underscore! i put nextidx here and it took a while to find that bug
        else:
            return word
    else:
        return None
       

'''
T: W*L
S: LW but could be L + W

fis
f***i*****s*****

T: L + k*W + k*W = L + k * W
S: kW + L but could be W + L
'''
def hashmap_find_scrambled(words: List[str], string:str) -> Optional[str]:
    stringcounter = Counter(string) #L
    wordcounter = {}
    for word in words:
        wordcounter[word] = Counter(word) # L * W;  space: LW
    for item in wordcounter.items(): # W * L
        word, counter = item
        for letter in word:
            if counter[letter] > stringcounter[letter]:
                break
        else:
            return word
    return None

'''
fis
f***i*****s*****
W: length of each word
L: string length
k: number of words

T: L lg L + k*(W lg W + (W + L) )
S: L lg L + W lg W
'''
def subseq_find_scrambled(words: List[str], string:str) -> Optional[str]:
    string = sorted(string) #tcabnihjs -> abchijnst
    for word in words: #cat -> act
        listword = sorted(word)
        widx = stringidx = 0
        while widx < len(listword) and stringidx < len(string):
            if listword[widx] == string[stringidx]:
                widx, stringidx = widx + 1, stringidx + 1
            else:
                stringidx += 1
        if widx == len(listword):
            return word
    return None

'''
fis
f***i*****s*****

complexity same as above
'''
def forsubseq_find_scrambled(words: List[str], string:str) -> Optional[str]:
    liststring = sorted(string) #tcabnihjs -> abchijnst
    for word in words: #cat -> act
        listword = sorted(word)
        nextidx = 0
        for letter in listword:
            for idx, stringletter in enumerate(liststring[nextidx:], nextidx):
                if stringletter == letter:
                    nextidx = idx + 1
                    break
            else: #listword is not a subsequence
                break
        else:
            return word
    return None
    
words = ["cat", "baby", "dog", "bird", "car", "ax"]
strings = ["tcabnihjs"
    , "tbcanihjs"
    , "baykkjl"
    , "bbabylkkj"
    , "ccc"
    , "breadmaking"
    , "xavier"
    , ""
    ]
results = ["cat", "cat", None, "baby", None, "bird", "ax", None]
find_scrambled_methods = (
    hashmap_find_scrambled
    , subseq_find_scrambled
    , forsubseq_find_scrambled
    , binsearch_find_scrambled
    )
for string, result in zip(strings, results):
    for find_scrambled in find_scrambled_methods:
        findresult = find_scrambled(words, string)
        print(find_scrambled.__name__, findresult, result, string)
        assert(findresult == result)
    print()