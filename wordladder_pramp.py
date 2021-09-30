'''
consider one letter change at a time and advance in BFS only if changed is in words
keep track of bfs path length
BFS
  mark nodes you've seen as you go to prevent cycles
  stop entirely when you get to target
But as a challenge, run through the code manually first ... or after the change actually!
'''
from collections import deque
def shortestWordEditPath(source, target, words):
  
  '''
  fish ... aish ... bish ...
  '''
  def neighbors(word):
    newword = list(word)
    for i in range(len(word)):
      ignorech = word[i]
      for j in range(26):
        ch = chr(j + ord('a'))
        if ch != ignorech:
          newword[i] = ch
          newword_str = ''.join(newword)
          if newword_str in wordsset and newword_str not in visit:
            yield newword_str
      newword[i] = ignorech

  wordsset = set(words)
  visit = set()
  q = deque([source])
  visit.add(source)
  count = 0
  while q:
    for i in range(len(q)):
      word = q.popleft()
      if word == target:
        return count
      for nextword in neighbors(word):
        q.append(nextword)
        visit.add(nextword)
    count += 1
  return -1