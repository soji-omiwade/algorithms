'''
arr = ['x','y','z'], str = "xyyzyzyx"


>>> set(["A"]) in set("A")
False

str = "xxxyyz"
'''

'''
A.issubset(B)

ADOBECODEBANCDDD
'''


'''
I can't hear or see you either!

yes agree. maybe I can finish with typed hints if needed :-)


Sorry I cannot hear you and see you...
I wonder if we can reconnect, but I think we can keep chating a few words
in text lol~
Sure
You are already almost there, 
haha
Sure

Yayy lloks like I got it. THANK YOU!! HAHA. oh wow. really? thx!a
haha thx. ok cool my pancake soln is same as urs. so no need. but can u tell me complexity of pancake b4 we wrap up
yep. fun fact: i think bill gates came up with it. 

ok so for your problem: complexity.. let me look..
it looks like m*n to me. because of O(1) dict access/edit


yeah one more part the set let me try.
You can try, maybe after some time I can show you my solution here. almost the same.

no i don't think so :-)
each time you go through. when u look in dict, that is O(len(arr)), right? this is nested. yeah
i thot so.

Good job!!!
This is a hard problem actually, haha!
I will put my solution here for your reference, But I think you did a even better job!
Sure I think the time complexity is n + n-1 + n-2 ... so I guess it is O(n^2)
Haha that's hilarious!
You want to add each other on Linkedin?
Maybe I can have more feed back for you latter
yes, but not quite, you only went through arr once to build the array and go through the str once
Maybe your time complexity is O(M+N)
O yeah, for your function yes, that part may be improved a little haha.

I put my code here for your reference, but it is the same with the answer in the page, you will see later.
by checking the length of the unique characters can improve the checking the validity of the substring.
Your thought is very clear and put everything part by part that is really great! haha

thank you. man. ok. you did good job too. i have to run now. thx for the time!

Sure thank you very much! you did a very good job too! Thanks! Have a good night you too!!!

My name is Chenxi Zhang, you can find me on linkedin if you want we can have further communication!
Have a good nit
Mine is Soji: 

okay thanks.
import collections
def get_shortest_unique_substring(arr, str):
    left = 0
    cur_counter = {}
    unique_char_num = 0
    res = ""
    # Initialize the counter for the string in the window
    for char in arr:
        cur_counter[char] = 0
        
    for right in range(len(str)):
        if str[right] not in cur_counter:
            continue
        if cur_counter[str[right]] == 0:
            unique_char_num += 1
        cur_counter[str[right]] += 1
        
        while unique_char_num == len(arr):
            cur_length = right - left + 1
            if cur_length == len(arr):
                return str[left:right+1]
            
            if cur_length < len(res) or res == "":
                res = str[left:right+1]
                
            if str[left] in cur_counter:
                cur_counter[str[left]] -= 1
                if cur_counter[str[left]] == 0:
                    unique_char_num -= 1
            left += 1
    return res



'''
from collections import defaultdict
def arr_in_dict(arr, d):
  for x in arr:
    if x not in d.keys():
      return False
  return True

def get_shortest_unique_substring(arr, str):
  m, n = len(arr), len(str)
  i = 0
  d = defaultdict(int)
  min_len = float('inf')
  im = 0
  for j in range(n): # str
    d[str[j]] += 1
    while arr_in_dict(arr, d):
      if j-i+1 < min_len:
        im = i
        min_len = j-i+1
      d[str[i]] -= 1
      if d[str[i]] == 0:
        del d[str[i]]
      i += 1
  print(min_len, im)
  if min_len == float('inf'):
    return ''
  return str[im:im+min_len]
      
    