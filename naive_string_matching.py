def foo(pattern, text):
    for i in range(len(text)):
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                break
        else:
            return True
    return False
    
import sys
print(foo(sys.argv[1],sys.argv[2]))