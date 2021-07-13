'''BFS time complexity
conventional: n^2 * m = 25m * 10 =  250m
plus preprocessing with alphabet of size ksi, all n : m*n*ksi + n^2 = 10*26*5k + 25m = 26m; 
    note: is big-omega of n*ksi
with ksi, but no preprocessing: m*n*ksi = 10 * 5k * 26 = 1.3m 
    note: doesn't have the big-omega component!
    
    
start: 9am
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
what if we come from the start word and endword. could that be faster? 
algo:
    todo = set of wordList
    left = set(beginWord)
    right = set(endWord)
    
    hit-hot-hoa-boa
    l           r
    hot-hoa-boa
    l           r
    ladderlen = 2
    while todo
        optimize on who is left and who is right (later...)
        for word in left
            if word in right
                return ladderlen
        put all neighbors of all nodes in left in left; remove them from todoo accordingly
        ladderlen += 1
    return 0        
hat 
'''
from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_children_into_left(word, left, todo):
            for j in range(len(word)):
                otherword = word
                for i in range(ord("a"), 1 + ord("z")):
                    ch = chr(i)
                    otherword = otherword[:j] + ch + otherword[j+1:]
                    if otherword in todo:
                        left.add(otherword)
                        todo.remove(otherword)

        todo = set(wordList) | set([beginWord])       
        todo.remove(beginWord)
        # todo.remove(endWord)
        # if not todo:
        #     todo.add(endWord)
        left = set([beginWord])
        right = set([endWord])
        
        '''
        hit-hot-hoa-boa
        l           r
        hot-hoa-boa
        l       r
        hoa-boa
        l   r
        '''
        ladderlen = 2
        '''
        left = hit
        right = cog
        wordlist = ["hot","dot","dog","lot","log","cog"]
        todo = [hot, "dot","dog","lot","log"]
        '''
        while left:
            # print(left)
            #optimize on who is left and who is right (later...)
            #put all neighbors of all nodes in left in left; remove them from todo accordingly; remove node from left
            for word in left.copy():
                left.remove(word)
                get_children_into_left(word, left, todo) # get children of word and put them in left; adjust todo accordingly
            for word in left:
                if word in right:
                    return ladderlen
            ladderlen += 1
        return 0        
