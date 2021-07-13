'''BFS time complexity
conventional: n^2 * m = 25m * 10 =  250m
plus preprocessing with alphabet of size ksi, all n : m*n*ksi + n^2 = 10*26*5k + 25m = 26m; 
    note: is big-omega of n*ksi
with ksi, but no preprocessing: m*n*ksi = 10 * 5k * 26 = 1.3m 
    note: doesn't have the big-omega component!
'''
from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        todo = deque([beginWord])
        unvisited = set(wordList)
        unvisited.add(beginWord)
        unvisited.remove(beginWord) #gone: hit, hot        
        ans = {beginWord: 1}
        while todo:
            word = todo.popleft() #hit
            if word == endWord:
                return ans[word]            
            for i in range(len(word)):
                for j in range(ord('a'), ord('z') + 1):
                    ch = chr(j)
                    childword = word[:i] + ch + word[i+1:]
                    if childword in unvisited:
                        ans[childword] = ans[word] + 1
                        todo.append(childword)
                        unvisited.remove(childword) #gone: hit, hot
                        # print('processed: ', word, childword, unvisited, todo)
        return 0