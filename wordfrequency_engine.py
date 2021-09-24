from typing import List, Tuple

'''
approach: 
    clean out each word from non alphanum characters
    initialize a counter (note that the order from left to right is actually preserved)
        Ill 1, be 3, starting 1, ...
    create a array res, with length len(sen), with empty lists, 
    for each word, freq in counter
        res[freq].append(word)
    finalres = []
    for freq, lis in enumerate(res):
        for word in lis:
            finalres.append([word, str(freq)])
    return finalres
'''
def wordorder(sen: str) -> List[Tuple[str, str]]:
    ...
    
sen = "I'll be starting at an exciting startup, guys!!"
print(wordorder(sen)) #[("Ill", "1"), ("be", "1"), ...]

sen = "I'll be be be starting at an an exciting startup, guys!!"
print(wordorder(sen)) #[("be", "3"), ("an", "2"), ("Ill", "1"), ("starting", "1"), ...]

sen = ""
print(wordorder(sen)) #[]
