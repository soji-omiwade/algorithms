from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def onestep(word, otherword):
            step = 0
            for let, otherlet in zip(word, otherword):
                if let != otherlet:
                    step += 1
                    if step > 1:
                        return False
            return step == 1
        
        unprocessed_words = deque([beginWord])
        distance = defaultdict(int)
        wordList_set = set(wordList)
        wordList_set.add(beginWord)
        #complexity =                                               n^2 * m = 25m * 10 =  250m
        #could be made =                                            n*ksi + n^2 = ???   this one is big-omega of n * ksi
        #another way is quite interesting: no preprocessing         n*ksi +            this one doesn't have the big-omega component!
        while unprocessed_words:
            word = unprocessed_words.popleft()
            wordList_set.remove(word)
            for otherword in wordList_set:
                if distance[otherword] == 0 and onestep(word, otherword):
                    if otherword == endWord:
                        return distance[word] + 2
                    distance[otherword] = 1 + distance[word]
                    unprocessed_words.append(otherword)
        if distance[endWord] != 0:
            return distance[endWord] + 1
        return 0

    
    # if word == endWord:
            #     return distance[word]
            