# Given a 2D grid and a word, write a function that returns the location of the word in the grid as a list of coordinates.
# The word may start anywhere in the grid, and consecutive letters can be either immediately below, or immediately to the right of the previous letter.
# If there are multiple matches, return any one.


'''
function search(grid, word, idx=0)
    for row in rows in grid
        for col in cols in the grid
            if grid[row][col] == word[idx]
                
            search()
'''

# grid1 = [
# 	['c', 'c', 'x', 't', 'i', 'b'],
# 	['c', 'c', 'a', 't', 'n', 'i'],
# 	['a', 'c', 'n', 'n', 't', 't'],
# 	['t', 'c', 's', 'i', 'p', 't'],
# 	['a', 'o', 'o', 'o', 'a', 'a'],
# 	['o', 'a', 'a', 'a', 'o', 'o'],
# 	['k', 'a', 'i', 'c', 'k', 'i'],
# ]
# word1 = "catnip"
# word2 = "cccc"
# word3 = "s"
# word4 = "bit"
# word5 = "aoi"
# word6 = "ki"
# word7 = "aaa"
# word8 = "ooo"

# grid2 = [['a']]
# word9 = "a"

# find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
# find_word_location(grid1, word2) =>
#        [(0, 1), (1, 1), (2, 1), (3, 1)]
#     OR [(0, 0), (1, 0), (1, 1), (2, 1)]
#     OR [(0, 0), (0, 1), (1, 1), (2, 1)]
#     OR [(1, 0), (1, 1), (2, 1), (3, 1)]
# find_word_location(grid1, word3) => [(3, 2)]
# find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
# find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
# find_word_location(grid1, word6) => [(6, 4), (6, 5)]
# find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
# find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
# find_word_location(grid2, word9) => [(0, 0)]
def findcoord(grid, word):
    coord = []
    def search(row, col, word):
        if word == "":
            return True
        if row >= len(grid) or col >= len(grid[0]) or grid[row][col] != word[0]:
            return False
        # print(row, col, grid[row][col], word)
        coord.append((row, col))
        search2 = search(row, col + 1, word[1:])
        if search2:
            return True
        search1 = search(row + 1, col, word[1:])
        if search1:
            return True
        coord.pop()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # print()
            if search(row, col, word):
                return coord
    raise Exception("word exists")

grid1 = [
	['c', 'c', 'x', 't', 'i', 'b'],
	['c', 'c', 'a', 't', 'n', 'i'],
	['a', 'c', 'n', 'n', 't', 't'],
	['t', 'c', 's', 'i', 'p', 't'],
	['a', 'o', 'o', 'o', 'a', 'a'],
	['o', 'a', 'a', 'a', 'o', 'o'],
	['k', 'a', 'i', 'c', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

print(findcoord(grid1, word1))
print(findcoord(grid1, word2))
print(findcoord(grid1, word3))
print(findcoord(grid1, word4))
print(findcoord(grid1, word5))
print(findcoord(grid1, word6))
print(findcoord(grid1, word7))
print(findcoord(grid1, word8))


grid2 = [['a']]
word9 = "a"

print(findcoord(grid2, word9))






'''
T: W*L
S: LW but could be L + W
'''
words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"

from typing import List
from collections import Counter

'''


def find_scrambled(words: List[str], string:str):
    stringcounter = Counter(string) #L
    wordcounter = {}
    for word in words:
        wordcounter[word] = Counter(word) # L * W;  space: LW
    #print(wordcounter)    
    for item in wordcounter.items(): # W * L
        word, counter = item
        for letter in word:
            if counter[letter] > stringcounter[letter]:
                break
        else:
            return word
    return None
words = ["cat", "baby", "dog", "bird", "car", "ax"
        
        ]
string1 = "tcabnihjs"
print(find_scrambled(words, string6))
'''