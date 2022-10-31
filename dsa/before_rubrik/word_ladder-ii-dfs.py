'''
start: 9:06am
end:...
io
aa
dd
[ab cb db dd]
output: [aa ab cb dd], [aa ab db dd]
diagram
constraints
    
pseudo
use dfs since we must consider all routes:
BUT we should find neighbors via the alphabet to save space
python's yield can help with better implementation!

todo = set(wordList)
todo.add(beginWord)
res = []
dfs(beginWord, res, [])
return res

function unvisited_neighbors(word)
    for i in [0..len(word))
        for each ch in in a - z
            otherword = word[:i] + ch + word[i+1:]
            if otherword in todo
                yield otherword
                

function dfs(word, res, path)
    path.add word
    todo.remove(word)

    if word is endWord
        append (path).copy to res
    else
        for all unvisited_neighbors nb of word
                dfs(nb, res, path)
    todo.add(word)
    path.remove(word)    
        
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def unvisited_neighbors(word):
            for i in range(len(word)):
                for ord_ in range(ord("a"), ord("z") + 1):
                    otherword = word[:i] + chr(ord_) + word[i+1:]
                    if otherword in todo:
                        yield otherword

        def dfs(word):
            path.append(word)
            todo.remove(word)
            if word == endWord:
                res.append(path[:])
            else:
                for otherword in unvisited_neighbors(word):
                    dfs(otherword)
            todo.add(word)
            path.remove(word)    

        todo = set(wordList + [beginWord])
        # if endWord not in todo:
        #     return []
        res = []
        path = []
        dfs(beginWord)
        if res:
            minlen = min(len(path) for path in res)
            res = [path for path in res if len(path) == minlen]
        return res
