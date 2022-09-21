'''
start: 6:52am
end: 7:57

i/o:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

diagram
hit, hot dot lot, dog, cog ...
constraints

pseudocode
parent lookup: collect all results
for this, we use lookup to build the parent lookup
'''
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def update_result():
            curr = endWord
            subres = []
            while curr is not None:
                subres.append(curr)
                curr = parent[curr]
            res.add(tuple(reversed(subres)))

        todo = set(wordList)
        if endWord not in todo:
            return []
        level = deque([beginWord])
        todo.discard(beginWord)
        todo.remove(endWord)
        parent = {beginWord: None}
        res = set([])
        while level: #hit
            for _ in range(len(level)):
                word = level.popleft() #hit
                for j in range(len(word)):
                    for k in range(ord("a"), ord("z") + 1):
                        otherword = word[:j] + chr(k) + word[j + 1:]
                        if otherword in todo:
                            parent[otherword] = word
                            todo.remove(otherword)
                            level.append(otherword)
                        elif otherword == endWord:
                            parent[otherword] = word
                            update_result()
        shortestlen = min(len(subres) for subres in res) if res else 0
        for subres in res.copy():
            if len(subres) > shortestlen:
                res.remove(subres)
        return [item for item in res]