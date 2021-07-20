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
            length = 0
            level = deque([beginWord])
            while level:
                length += 1
                for _ in range(len(level)):
                    word = level.popleft()
                    for letidx in range(len(word)):
                        for alphidx in range(ord('a'), ord('z') + 1):
                            ch = chr(alphidx)
                            otherword = word[:letidx] + ch + word[letidx + 1:]
                            if otherword in wordList:
                                level.append(otherword)
                                nbs[word].append(otherword)
                                nbs[otherword].append(word)            
                                if otherword == endWord:
                                    return length
            return None
        '''
        length = 0
        word = bw -> ow (not ew)
        ow = not ew
        '''
        def dfs(word, path):
            nonlocal length
            if length == 0:
                return
            
            if word == endWord:
                result.append(path[:])
            else:
                for otherword in nblookup[word]:
                    if otherword in todo:
                        todo.remove(otherword)
                        path.append(otherword)
                        length -= 1
                        dfs(otherword)
                        length += 1
                        path.pop()
                        todo.add(otherword)
                    
        
        result = []
        nblookup = defaultdict(list)
        length = bfs()
        if not length:
            return []
        todo = set(wordList)
        dfs(beginWord, [beginWord])
        
        return result