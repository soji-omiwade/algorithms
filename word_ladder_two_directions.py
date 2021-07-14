'''
move along two sets opposite directions, but only on the smaller one each time
stop when, during discovery, we see a node in the other set
also stop when either head or tail is exhausted --> the sets couldn't reach each other and hence bw cant get to ew
never start if endword is not even in wordlist, since the two sets can reach each other even so, which would be wrong

hit-hot-bot
h        t

input:
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
head = {dot, lot}
tail = {cog}
ladderlen = 4

hit - hot - dot - dog \ 
             |     |    cog
            lot - log /
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        head = set([beginWord])
        tail = set([endWord])
        words.remove(endWord)
        words.discard(beginWord)
        ladderlen = 2
        while head and tail:
            if len(head) > len(tail):
                head, tail = tail, head
            for word in head.copy():
                head.remove(word)
                for i in range(len(word)):
                    for j in range(ord('a'), ord('z') + 1):
                        otherword = word[:i] + chr(j) + word[i+1:] # ait
                        if otherword in tail:
                            return ladderlen
                        if otherword in words:
                            head.add(otherword)
                            words.remove(otherword)
                        otherword = word
            ladderlen += 1
        return 0