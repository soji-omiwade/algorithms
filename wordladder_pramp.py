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
  def getnext(word):
    newword = list(word)
    for i in range(len(word)):
      ignorech = word[i]
      for j in range(26):
        ch = chr(j + ord('a'))
        if ch != ignorech:
          newword[i] = ch
          if ''.join(newword) in wordsset:
            yield newword
      newword[i] = ignorech

  wordsset = set(words)
  q = deque([source])
  count = 0
  while q:
    for i in range(len(q)):
      word = q.popleft()
      for nextword in getnext(word):
        q.append(nextword)
    count += 1
  return count