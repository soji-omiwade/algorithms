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
def word_count_engine(document):
  pass # your code goes here