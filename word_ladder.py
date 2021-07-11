from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def onestep(word, otherword):
            step = 0
            for let, otherlet in zip(word, otherword):
                if let != otherlet:
                    step += 1
            return step == 1
        
        unprocessed_words = deque([beginWord])
        distance = defaultdict(int)
        while unprocessed_words:
            word = unprocessed_words.popleft()
            for otherword in wordList:
                if distance[otherword] == 0 and onestep(word, otherword):
                    distance[otherword] = 1 + distance[word]
                    unprocessed_words.append(otherword)
        if distance[endWord] != 0:
            return distance[endWord] + 1
        return 0

    
    # if word == endWord:
            #     return distance[word]
            