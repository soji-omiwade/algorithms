'''
3:29pm -- 
constraint
    s is non-empty

for each word check issubseq(word, s) and accrue the count as result

function issubseq(word, string)
    make both stacks
    while both stacks still have something   <-- break when one is empty
        ch = pop char from word
        pop from string until ch found. then break
    if word is not empty
        return False
    else 
        return True
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(word, string):
            '''
            a c e
                ^
            a b c d e
                      ^
            '''
            sidx = 0
            for ch in word:
                #print(ch, sidx)
                while sidx < len(string) and string[sidx] != ch:
                    sidx += 1
                if sidx == len(string):
                    return False
                sidx += 1
            return True
        
        count = 0
        lookup = {}
        for word in words:
            if word in lookup:
                if lookup[word]:
                    count += 1
            else:
                if issubseq(word, s):
                    count += 1
                    lookup[word] = True
                else:
                    lookup[word] = False
        return count