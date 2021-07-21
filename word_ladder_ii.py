'''
2. use BFS to find shortest length
    a. establish neighbors: go through alphabet, change 1 letter, if in wordList, 
        add neighbor to dict for this word
        
    b. BFS -- add that nb word to queue
    c. stop BFS when endWord is found.
    d. return length
    
3. use DFS to find routes with shortest length
    optimization detail: - i --> nbs(i)  ==> consider neighbors that are distance one further away from start
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def bfs():
            todo = set(wordList)
            todo.add(beginWord)            
            allwords = set(wordList)
            count = 0
            level = deque([beginWord])
            todo.remove(beginWord)
            length = None
            while level:
                count += 1
                for _ in range(len(level)):
                    word = level.popleft()
                    if word == endWord:
                        length = count                
                    for letidx in range(len(word)):
                        for alphidx in range(ord('a'), ord('z') + 1):
                            ch = chr(alphidx)
                            otherword = word[:letidx] + ch + word[letidx + 1:]
                            if otherword in allwords - set([word]):
                                nblookup[word].add(otherword)
                                nblookup[otherword].add(word)                                
                            if otherword in todo:
                                level.append(otherword)
                                todo.remove(otherword)
            return length
        '''
        length = 0
        word = bw -> ow (not ew)
        ow = not ew
        '''
        def dfs(word, path):     # word = hat
            nonlocal length      # 2 1 0 
            todo.remove(word)    # [hut hot]
            path.append(word)    # [hit hat] 
            length -= 1          
            if length != -1: 
                if word == endWord: #endword = hot
                    result.append(path[:])
                else:
                    for otherword in nblookup[word]:
                        if otherword in todo:
                            dfs(otherword, path)
            length += 1
            path.pop()
            todo.add(word)
            
        from pprint import pprint                                  
        result = []
        nblookup = defaultdict(set)
        length = bfs()
        # pprint(nblookup)
        # print(length)
        if length is None:
            return []
        
        todo = set(wordList)
        todo.add(beginWord)
        dfs(beginWord, [])        
        return result