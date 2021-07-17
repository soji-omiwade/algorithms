'''
time: 11:36m
end: 

io
beginWord = hit
end word = cog
wordList = [hot, dot, dog, lot, log, cog]
constraints
diagram
pseudocode
BFS to find length of shortest sequence, minlen
Then DFS to:
i. find all sequences of length, minlen
ii. stop any sequence that is more than minlen [optimization for later]

queue = [beginWord]
minlen = 1
todo = set(wordList)
todo.add(beginWord)
while queue has elements
    count = len(queue)
    minlen += 1
    for i in range(count)  ---> O(n)
        word = popleft
        if word is endword
            return minlen
        for all neighbor, otherword, of word, NOT in todo O(n *m)
            push into queue otherword
            todo.remove(otherword)
return minlen

t: O(m * n^2)
s: O(m)
t-better: O(n * m * ksi)

'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def BFS() -> int:
            queue = deque([beginWord]) # [hit]
            minlen = 1
            while queue:
                minlen += 1      #2
                for _ in range(len(queue)): #  ---> O(n)
                    word = queue.popleft() #hit
                    if word == endWord:
                        return minlen
                    for i in range(len(word)):
                        for j in range(ord('a'), 1 + ord('z')):
                            otherword = word[i:] + chr(j) + word[i+1:]
                            if otherword in todo:
                                queue.append(otherword)
                                todo.remove(otherword)
            return minlen
        
        todo = set(wordList)
        if endWord not in todo or len(todo) == 1:
            return []    
        todo.discard(beginWord) # so we can always use remove
        minlen = BFS()
        print(minlen)
        # paths = DFS()
        # return paths
