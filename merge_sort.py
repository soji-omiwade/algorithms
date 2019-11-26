import unittest
import random
import time
def merge(a, p, r):
    i,j = p,(p+r)//2
    b = []
    #p,r = 3,5; a[p:r] = [6,1]
    while True:
        x = a[i] if i < (p+r)//2 else None
        y = a[j] if j < r else None
        
        if x is None and y is None:
            break
        if x is not None and y is not None:
            if x < y:
                b.append(a[i])
                i += 1
            else:
                b.append(a[j])
                j += 1
        elif x is not None:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
    for i in range(len(b)):
            a[p+i] = b[i]
    # print("after merge: ", a[p:r], b)
    # time.sleep(3)       
    
def run(a):
    def merge_sort(a, p, r):
        #expect at least two elements,  since otherwise it's sorted
        if r > p + 1:
            merge_sort(a, p, (p+r)//2)
            merge_sort(a, (p+r)//2, r)
            merge(a, p, r)
    merge_sort(a, 0, len(a))



class MyTest(unittest.TestCase):
    def test(self):
        a = [random.randrange(0,1000) for _ in range(1)]
        self.assertNotEqual(sorted(a), a)
        run(a)
        self.assertEqual(sorted(a), a)

if __name__ == '__main__':
    unittest.main()