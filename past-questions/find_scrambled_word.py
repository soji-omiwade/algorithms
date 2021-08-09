'''
T: W*L
S: LW but could be L + W
'''
words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"

from typing import List
from collections import Counter


def find_scrambled(words: List[str], string:str):
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
words = ["cat", "baby", "dog", "bird", "car", "ax"
        
        ]
string1 = "tcabnihjs"
print(find_scrambled(words, string6))