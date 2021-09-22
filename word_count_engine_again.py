'''

lookup[word] --> count

for word in words: #n is the number of words
  lookup[word] += 1
raw_result = sorted(lookup, key=lambda x: lookup[x])
return result

T: O(n log n) NLogN O(N) M < 2000
S: O(n) <--- N M(unique words)
   O(m) N words, M:len of the word;

p 3, pr 2, mk 1, M （1 ，M）

minFreq maxFreq
million    million + 5      100
        freq
map<int,vector<string>>   ---> OrderedDict

2 4 5 8  logN  m * lg m  +  m


for i = min to the maxkey
  if map[i] --> O(1)
    ...
    
    
(difference) 100 bucket
 
 bucket array. 
declare
0 .2    ..3
   [perf, ]      [practice]


for bucket, idx in reversed(buckets)
  for word in bucket
    result.append(word, str(idx))
    
constraints:
case should be ignored
space delimted
'''
from collections import Counter
def word_count_engine(string):
    def remove_puncts(string):
        res = ""
        for ch in string:
            if "a" <= ch <= "z" or ch == " ":
                res += ch
        return res

    string = remove_puncts(string.lower())
    res = Counter(string.split(" "))
    res = { key: (-value, ord_) for ord_, (key, value) in enumerate(res.items())}
    # print(res)
    res = sorted(res.items(), key=lambda item: item[1])
    print(res)
    return [[key, str(-value[0]) ] for key, value in res]
  
#document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
document = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
print(word_count_engine(document))