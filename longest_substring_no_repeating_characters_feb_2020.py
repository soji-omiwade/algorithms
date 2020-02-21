def longest_charset_based(s):
    next_loc=[0]*128
    im,jm=1,0; i=0
    for j in range(len(s)):
        i=max(i,next_loc[ord(s[j])])
        next_loc[ord(s[j])]=j+1
        if j-i>jm-im:
            im,jm=i,j
    return im,jm,s[im:jm+1]


def longest_dict_based(s):
    d={}
    i=0
    im,jm=1,0
    for j in range(len(s)):
        if s[j] in d:
            i=max(i,d[s[j]])
        d[s[j]]=j+1
        if j-i>jm-im:
            im,jm=i,j
    return im,jm,s[im:jm+1]
"""
s="abcdcbkkek"
res="bcda"
"""
def longest_substring_no_repeating_chars_set(s):
    """
    time: O(n)
    """
    i=0
    st=set([])
    im,jm=1,0
    for j in range(len(s)):
        if s[j] in st:
            for i in range(i,j):
                st.remove(s[i])
                if s[i] == s[j]:
                    i+=1
                    break
        st.add(s[j])
        if j-i>jm-im:
            im,jm=i,j
    return im,jm,s[im:jm+1]

s="abcdabkkek"
print(longest_substring_no_repeating_chars_set(s))
assert  (longest_substring_no_repeating_chars_set(s) 
            == longest_dict_based(s)
            == longest_charset_based(s))

import sys
s=sys.argv[1]
print(longest_substring_no_repeating_chars_set(s))
assert  (longest_substring_no_repeating_chars_set(s) 
            == longest_dict_based(s)
            == longest_charset_based(s))
