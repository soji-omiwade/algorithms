from typing import List, Tuple
from collections import Counter
'''
approach: 
    clean out each word from non alphanum characters
    initialize a counter (note that the order from left to right is actually preserved)
        Ill 1, be 3, starting 1, ...
    create a array res, with length len(sen), with empty lists
    go through each word (and its frequence) in the counter and append it to the result at res[freq]
    final result is outputing the contents of the sublists starting from the back!
'''
def wordorder(sen: str) -> List[Tuple[str, str]]:
    if not sen:
        return []
    sen = ["".join(letter for letter in word if letter.isalnum()) for word in sen.split(" ")]
    counter = Counter(sen)
    res = [[] for _ in range(1 + len(sen))]
    for word, freq in counter.items():
        res[freq].append(word)
    
    finalres = []
    for freq, lis in enumerate(reversed(res)):
        tfreq = len(res) - 1 - freq
        for word in lis:
            finalres.append([word, str(tfreq)])
    return finalres
    
sen = "I'll be starting at an exciting startup, guys!!"
print(wordorder(sen)) #[("Ill", "1"), ("be", "1"), ...]

sen = "I'll be be b^e star7ting at an an exciting startup, guys!!"
print(wordorder(sen)) #[("be", "3"), ("an", "2"), ("Ill", "1"), ("starting", "1"), ...]

sen = ""
print(wordorder(sen)) #[]

sen = "I'll"
print(wordorder(sen)) #[("Ill", 1)]
